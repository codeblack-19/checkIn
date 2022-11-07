from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from chat_group.models import ChatGroup
from chat_members.models import ChatGroupMembers

from .models import Chat
from .serializers import ChatSerializer

# new chat message
class NewChatMessage(generics.CreateAPIView):
    queryset = Chat.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        group_intance = ChatGroup.objects.filter(pk=self.request.data['group']).first()
        if group_intance:
            if not ChatGroupMembers.objects.filter(group=group_intance, user=self.request.user,).first():
                raise ValidationError({'detail': "You're not a member of the group"})
        else :
            raise ValidationError({'detail': "Group does not exist"})

        serializer.save(group=group_intance, user=self.request.user,)
        return super().perform_create(serializer)


# delete chat message
class DeleteChatMessage(generics.DestroyAPIView):
    queryset = Chat.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChatSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)