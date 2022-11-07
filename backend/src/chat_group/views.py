from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated

from chat import models as chat_models, serializers as chat_serializers
from .models import ChatGroup

from .serializers import ChatGroupSerializer

# get all groups
class ChatGroupListAPIView(generics.ListAPIView):
    queryset = ChatGroup.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = ChatGroupSerializer

# create new group
class ChatGroupCreateAPIView(generics.CreateAPIView):
    queryset = ChatGroup.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChatGroupSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

# update group
class ChatGroupUpdateAPIView(generics.UpdateAPIView):
    queryset = ChatGroup.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChatGroupSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        return super().perform_update(serializer)

# delete chat group
class ChatGroupDestroyAPIView(generics.DestroyAPIView):
    queryset = ChatGroup.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChatGroupSerializer
    lookup_field = 'id'

    def perform_destroy(self, instance):
        if instance.user != None and self.request.user != instance.user:
            raise serializers.ValidationError({'detail':'You are not the group creator'})

        return super().perform_destroy(instance)

# single group info
class ChatGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = ChatGroup.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChatGroupSerializer
    lookup_field = 'id'

# get all chat for a group by group Id
class GetChatByGroupId(generics.ListAPIView):
    queryset = chat_models.Chat.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = chat_serializers.ChatSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        group_intance = ChatGroup.objects.filter(pk=self.kwargs['id']).first()
        return chat_models.Chat.objects.all().filter(group=group_intance).order_by('createdAt')