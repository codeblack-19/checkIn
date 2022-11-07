from asyncore import read
from rest_framework import serializers

from api.serializers import ChatGhoupPublicSerializer, UserPublicSerializer
from .models import ChatGroupMembers

class GroupMembersSerializer(serializers.ModelSerializer):
    group = ChatGhoupPublicSerializer(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = ChatGroupMembers
        fields= [
            'group',
            'user',
            'createdAt'
        ]