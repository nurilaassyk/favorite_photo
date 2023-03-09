from rest_framework import serializers

from webapp.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'photo', 'created_at']
        read_only_fields = ['created_at']


