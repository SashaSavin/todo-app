from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'name': 'alex'
    }

    return render(request, 'main.html', context)

