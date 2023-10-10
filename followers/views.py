from rest_framework import generics, permissions
from drf_api.permissions import IsAccountOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(account_owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAccountOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer