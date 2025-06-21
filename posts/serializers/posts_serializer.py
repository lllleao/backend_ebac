from rest_framework import serializers
from ..models.post_user import Post, Comentario
from ..models.user import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'avatar', 'complet_name']


class ComentarioSerializer(serializers.ModelSerializer):
    autor = UsuarioSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'autor', 'post', 'texto', 'criado_em']


class PostSerializer(serializers.ModelSerializer):
    autor = UsuarioSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'autor', 'conteudo', 'criado_em']
