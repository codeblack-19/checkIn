from rest_framework import serializers

from api.serializers import UserPublicSerializer

from .models import ChatGroup

# chat groups serializer
class ChatGroupSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = ChatGroup
        fields = [
            'id',
            'user',
            'name',
            'group_desc',
            'createdAt',
        ]