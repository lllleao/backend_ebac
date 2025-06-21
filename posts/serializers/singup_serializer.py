from rest_framework import serializers
from ..models import Usuario

class UsuarioSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'is_active', 'email', 'password', 'complet_name']

    def create(self, validated_data):
        user = Usuario.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            complet_name=validated_data['complet_name']
        )
        return user
