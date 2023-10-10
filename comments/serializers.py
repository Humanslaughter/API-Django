from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    account_owner = serializers.ReadOnlyField(source='account_owner.username')
    is_account_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='account_owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='account_owner.profile.image.url')
    made_at = serializers.SerializerMethodField()
    edited_at = serializers.SerializerMethodField()

    def get_is_account_owner(self, obj):
        request = self.context['request']
        return request.user == obj.account_owner

    def get_made_at(self, obj):
        return naturaltime(obj.made_at)

    def get_edited_at(self, obj):
        return naturaltime(obj.edited_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'account_owner', 'is_account_owner', 'profile_id', 'profile_image',
            'post', 'made_at', 'edited_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')