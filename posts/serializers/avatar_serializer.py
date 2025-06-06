from rest_framework import serializers
from django.core.exceptions import ValidationError
from ..models.user import Usuario

class AvatarSerializer(serializers.ModelSerializer):
    def validar_imagem(value):
        if not value.name.endswith(('jpg', 'jpeg', 'png', 'gif')):
            raise ValidationError('O arquivo deve ser uma imagem com extensão .jpg, .jpeg, .png ou .gif')
        if value.size > 5 * 1024 * 1024:  # Limite de 5MB
            raise ValidationError('O tamanho da imagem não pode ser maior que 5MB')
        return value
    
    avatar = serializers.ImageField(validators=[validar_imagem])

    class Meta:
        model = Usuario
        fields = ['avatar']

