from datetime import datetime, timezone

from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TodoSerializer, BaseTodoSerializer, UserSerializer
from .models import Todo, CustomUser


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = BaseTodoSerializer
    queryset = Todo.objects.select_related('user')
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user, is_active=True)
        return queryset
    

    @action(methods=['POST', 'PATCH', 'PUT'], detail=True)
    def complete(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.completed = not todo.completed
        todo.save()
        serializer = BaseTodoSerializer(todo)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST', 'PATCH', 'PUT'], detail=False, url_path='complete-all')
    def all_completed(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        is_completed = request.data.get('completed', False)
        for todo in queryset:
            todo.completed = is_completed
            todo.save()
        serializer = BaseTodoSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

# TODO: Сделать историю через экшены. История - неактивные тудушки. Юзер видит только своюю историю. Админ видит всё.
# TODO: Удалять завершенные todo - удаление делает неактивным(is_active = false). удаление через crud destroy во viewset