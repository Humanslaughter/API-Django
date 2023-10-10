from rest_framework import serializers
from posts.models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    account_owner = serializers.ReadOnlyField(source='account_owner.username')
    is_account_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='account_owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='account_owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_account_owner(self, obj):
        request = self.context['request']
        return request.user == obj.account_owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                account_owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'account_owner', 'is_account_owner', 'profile_id',
            'profile_image', 'made_at', 'edited_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
        ]