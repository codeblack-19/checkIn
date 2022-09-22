from django.urls import path, include

from .views import (
    ChatGroupCreateAPIView, 
    ChatGroupListAPIView, 
    ChatGroupUpdateAPIView,
    ChatGroupDestroyAPIView,
    ChatGroupDetailAPIView,
    GetChatByGroupId
)

urlpatterns = [
    path('', ChatGroupListAPIView.as_view(), name="all_groups"),
    path('new', ChatGroupCreateAPIView.as_view(), name="new_group"),
    path('<int:id>/', ChatGroupDetailAPIView.as_view(), name="detail_group"),
    path('<int:id>/update', ChatGroupUpdateAPIView.as_view(), name="update_group"),
    path('<int:id>/delete', ChatGroupDestroyAPIView.as_view(), name="delete_group"),
    path('<int:id>/chat', GetChatByGroupId.as_view(), name="all_chats"),
    path('', include('chat_members.urls'))
]