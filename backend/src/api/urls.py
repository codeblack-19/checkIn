from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('group/', include('chat_group.urls')),
    path('chat/', include('chat.urls')),
]