from django.urls import path

from .views import GroupMembersLeaveGroup, GroupMembersListAPIView, GroupMemberCreateAPIView

urlpatterns = [
    path('<int:id>/members', GroupMembersListAPIView.as_view(), name="group_members"),
    path('<int:id>/join', GroupMemberCreateAPIView.as_view(), name="join_group"),
    path('<int:id>/leave', GroupMembersLeaveGroup.as_view(), name="leave_group")
]