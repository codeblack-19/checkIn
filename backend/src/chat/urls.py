from django.urls import path

from .views import DeleteChatMessage, NewChatMessage

urlpatterns = [
    path('', NewChatMessage.as_view(), name="new_message"),
    path('<int:id>/delete', DeleteChatMessage.as_view(), name="delete_message")
]