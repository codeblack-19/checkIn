from rest_framework import generics
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import ChatGroupMembers
from .serializers import GroupMembersSerializer
from chat_group.models import ChatGroup

# get group members
class GroupMembersListAPIView(generics.ListAPIView):
    queryset = ChatGroupMembers.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = GroupMembersSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        group_intance = ChatGroup.objects.filter(pk=self.kwargs['id']).first()
        return ChatGroupMembers.objects.all().filter(group=group_intance)


# join group
class GroupMemberCreateAPIView(generics.CreateAPIView):
    queryset = ChatGroupMembers.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = GroupMembersSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        group_intance = ChatGroup.objects.filter(pk=self.kwargs['id']).first()
        if ChatGroupMembers.objects.filter(group=group_intance, user=self.request.user,).first():
            raise ValidationError({'detail': "You can't join a group twice"})

        serializer.save(group=group_intance, user=self.request.user,)
        return super().perform_create(serializer)

# leave group
class GroupMembersLeaveGroup(generics.DestroyAPIView):
    queryset = ChatGroupMembers.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = GroupMembersSerializer
    lookup_field = 'id'

    def get_object(self):
        group_intance = ChatGroup.objects.filter(pk=self.kwargs['id']).first()
        return ChatGroupMembers.objects.all().filter(group=group_intance, user=self.request.user)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)