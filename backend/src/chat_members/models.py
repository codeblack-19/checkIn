from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
from chat_group.models import ChatGroup

# Create your models here.
class ChatGroupMembers(models.Model):
    group = models.ForeignKey(ChatGroup, db_column='pk', null=False, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [  
            models.UniqueConstraint(fields=['group','user'], name="unique_member")
        ]