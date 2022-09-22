from rest_framework import serializers

from api.serializers import UserPublicSerializer

from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only = True)
    class Meta:
        model = Chat
        fields = [
            'id',
            'user',
            'group',
            'text',
            'createdAt',
            'deletedAt',
        ]