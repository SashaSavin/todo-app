import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class UUidModelMixin(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, UUidModelMixin):
    pass

    def __str__(self):
        return self.username


class Todo(UUidModelMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= 'todos')
    text = models.CharField(max_length=50, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}, {self.id}'


