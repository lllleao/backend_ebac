from rest_framework import serializers
from ..models.user import Usuario

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['followers']
