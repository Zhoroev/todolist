from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    body = models.TextField()
    estimated_finish_time = models.DateTimeField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)