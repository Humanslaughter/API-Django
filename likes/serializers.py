from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    account_owner = serializers.ReadOnlyField(source='account_owner.username')

    class Meta:
        model = Like
        fields = ['id', 'made_at', 'account_owner', 'post']

    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})

