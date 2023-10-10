from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsAccountOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-made_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'account_owner__followed__account_owner__profile',
        'likes__account_owner__profile',
        'account_owner__profile',
    ]
    search_fields = [
        'account_owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__made_at',
    ]

    def perform_create(self, serializer):
        serializer.save(account_owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAccountOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-made_at')