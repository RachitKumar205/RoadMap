from django.urls import path
from .views import UserLoginAPIView, UserRegistrationAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('register/', UserRegistrationAPIView.as_view(), name="register")
]