from rest_framework import serializers
from . import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user',
            'text',
            'completed',
        )
        model = models.Todo
