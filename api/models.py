from django.db import models

# Create your models here.
class Secret(models.Model):
    key = models.CharField(max_length=50, unique=True)
    encrypted_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.key