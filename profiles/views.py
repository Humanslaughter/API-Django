from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsAccountOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('account_owner__post', distinct=True),
        followers_count=Count('account_owner__followed', distinct=True),
        following_count=Count('account_owner__following', distinct=True)
    ).order_by('-made_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'account_owner__following__followed__profile',
        'account_owner__followed__account_owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'account_owner__following__made_at',
        'account_owner__followed__made_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAccountOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('account_owner__post', distinct=True),
        followers_count=Count('account_owner__followed', distinct=True),
        following_count=Count('account_owner__following', distinct=True)
    ).order_by('-made_at')
    serializer_class = ProfileSerializer