from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, RegisterView

urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(), name="auth_login"),
    path('refresh', TokenRefreshView.as_view(), name="auth_refresh"),
    path('register', RegisterView.as_view(), name="auth_register")
]