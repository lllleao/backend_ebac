from rest_framework import serializers
from ..models.user import Usuario

class UpdateBioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['bio']
