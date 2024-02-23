from django.urls import path
from .views import UserRegistration

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    #path('user/', UserDetails.as_view(), name='user-details'),
]