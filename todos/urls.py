from django.urls import path
from . import views
from . views import UserCreate,  LoginView, lw, LogoutView


urlpatterns = [
    #front

    path('login/', views.lw.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='login'),

    # api

    path('api/all_todo_api', views.ListTodo.as_view()), # путь к апи всех todo
    path('api/todo_api/<int:pk>/', views.DetailTodo.as_view()),  #путь к отдельному todo
    path("api/users/", UserCreate.as_view(), name="user_create"),
    path("api/login/", LoginView.as_view(), name="login"),

]
