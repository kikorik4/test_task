from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import SecretInfo
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import  SecretInfoSerializer


class SecretInfoAPIList(ListCreateAPIView):
    queryset = SecretInfo.objects.all()
    serializer_class = SecretInfoSerializer
    permission_classes = IsAuthenticatedOrReadOnly,

class SecretInfoAPIUpdate(RetrieveUpdateAPIView):
    queryset = SecretInfo.objects.all()
    serializer_class = SecretInfoSerializer
    permission_classes = IsOwnerOrReadOnly,

class SecretInfoAPIDelete(RetrieveDestroyAPIView):
    queryset = SecretInfo.objects.all()
    serializer_class = SecretInfoSerializer
    permission_classes = IsAdminOrReadOnly,
