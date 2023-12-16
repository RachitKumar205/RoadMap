from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.

class UserRegistrationAPIView(APIView):

    def post(self, request):
        userserializer = UserSerializer(data=request.data)
        if userserializer.is_valid():
            userserializer.save()

        return JsonResponse({"message":"successfully registered user"})


class UserLoginAPIView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({
                'token': token.key,
                'pk': user.id,
                'username': user.username
            })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)




