import datetime

from rest_framework import serializers

from todos.models import CustomUser, Todo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'uuid',
            'username', 
            'email', 
            'password',
            'created',
            'modified',
        ]
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = CustomUser(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user


class BaseTodoSerializer(serializers.ModelSerializer):
    complete_time = serializers.SerializerMethodField()

    class Meta:
        fields = [
            'uuid',
            'user',
            'text',
            'completed',
            'complete_time',
            'date_completed'
        ]
        model = Todo

    def get_complete_time(self, obj):
        if obj.completed and obj.date_completed:
            return (obj.date_completed - obj.created).total_seconds()
        return "Not completed"


class TodoSerializer(BaseTodoSerializer):
    class Meta(BaseTodoSerializer.Meta):
        fields = BaseTodoSerializer.Meta.fields + [
            'created',
            'modified',
            'date_completed',
            'is_active',
        ]
