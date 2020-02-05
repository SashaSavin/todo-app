from rest_framework import serializers, generics
from . import models
from . models import CustomUser
from rest_framework.authtoken.models import Token


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user',
            'text',
            'completed',
        )
        model = models.Todo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = CustomUser(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


