import uuid
from datetime import datetime, timezone
from model_utils.models import TimeStampedModel

from django.db import models
from django.contrib.auth.models import AbstractUser


class UUIDModelMixin(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, UUIDModelMixin, TimeStampedModel):
    pass

    def __str__(self):
        return self.username


class Todo(UUIDModelMixin, TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= 'todos')
    text = models.CharField(max_length=50, blank=True)
    completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # delete or not
    date_completed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}, {self.id}'
        
    def save(self, *args, **kwargs):
        if self.completed:
            self.date_completed = datetime.now(timezone.utc)
        else:
            self.date_completed = None
        super().save(*args, **kwargs)