from django.urls import path
from . import views # импортируем views для использования в url patterns

urlpatterns = [
    path('', views.index), # привязываем в ссылке вьюху, чтобы по ссылке она сработала
]
