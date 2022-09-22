from django.db import models
from django.conf import settings
from datetime import datetime

User = settings.AUTH_USER_MODEL

# Create your models here.
class ChatGroup(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,)
    name = models.CharField(max_length=50, null=False, unique=True)
    group_desc = models.CharField(max_length=100, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)