from rest_framework import generics, permissions
from drf_api.permissions import IsAccountOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(account_owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAccountOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

