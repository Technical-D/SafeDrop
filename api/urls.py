from django.urls import path
from .views import CreateSecretView, RetrieveSecretView

urlpatterns = [
    path('create_secret/', CreateSecretView.as_view(), name='create_secret'),
    path('get_secret/<str:key>/', RetrieveSecretView.as_view(), name='get_secret'),
]
