from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import TodoViewSet


router = DefaultRouter()
router.register('todo', TodoViewSet)


urlpatterns = router.urls

