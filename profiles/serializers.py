from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    account_owner = serializers.ReadOnlyField(source='account_owner.username')
    is_account_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_account_owner(self, obj):
        request = self.context['request']
        return request.user == obj.account_owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                account_owner=user, followed=obj.account_owner
            ).first()
            # print(following)
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'account_owner', 'made_at', 'edited_at', 'name',
            'content', 'image', 'is_account_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]