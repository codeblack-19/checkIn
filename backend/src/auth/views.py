from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User


from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny,]
    serializer_class = MyTokenObtainPairSerializer

# register user view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer