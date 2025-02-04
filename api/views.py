from cryptography.fernet import Fernet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from datetime import timedelta
from .models import Secret

# Create your views here.
def encrypt_message(key, message):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(key, encrypted_message):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message.encode()).decode()

class CreateSecretView(APIView):
    def post(self, request):
        message = request.data.get('message')
        expires_in = int(request.data.get('expires_in', 3600))
        key = Fernet.generate_key()
        secret = Secret.objects.create(
            key=key.decode(),
            encrypted_message=encrypt_message(key, message),
            expires_at=now() + timedelta(seconds=expires_in)
        )
        return Response({"secret_url": request.build_absolute_uri(f"/api/get_secret/{key.decode()}/")})
    
class RetrieveSecretView(APIView):
    def get(self, request, key):
        try:
            secret = Secret.objects.get(key=key)

            if secret.expires_at and secret.expires_at < now():
                secret.delete()
                return Response({"error": "Secret has expired"}, status=404)

            message = decrypt_message(key.encode(), secret.encrypted_message)
            secret.delete()
            return Response({"message": message})
        except Secret.DoesNotExist:
            return Response({"error": "Secret not found or expired"}, status=404)
    
