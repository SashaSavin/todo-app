from django.urls import path
from . import views  # импортируем views для использования в url patterns

urlpatterns = [
    path('', views.index),  # привязываем в ссылке вьюху, чтобы по ссылке она сработала
    path('all_todo_api', views.ListTodo.as_view()),
    path('todo_api/<int:pk>/', views.DetailTodo.as_view()),
]
