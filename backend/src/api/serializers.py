from rest_framework import serializers

# user public data serializer
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)

# chat group public serializer
class ChatGhoupPublicSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)