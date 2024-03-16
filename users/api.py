from .models import User
from rest_framework import viewsets, permissions
from .serializer import AuthoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = AuthoSerializer