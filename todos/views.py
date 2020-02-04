from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers


# Create your views here.
from .models import Todo


def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'name': 'alex'
    }

    return render(request, 'main.html', context)


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
