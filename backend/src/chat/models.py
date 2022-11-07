from django.db import models
from django.conf import settings

from chat_group.models import ChatGroup

User = settings.AUTH_USER_MODEL

class Chat(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(ChatGroup, db_column='pk', null=False, on_delete=models.CASCADE)
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(default=None, null=True)