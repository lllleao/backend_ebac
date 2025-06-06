from rest_framework import serializers
from ..models.user import Usuario

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'bio', 'followers']
