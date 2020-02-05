from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from . import models
from . import serializers
from . serializers import UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView as lw
from django.contrib.auth.views import LogoutView


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


