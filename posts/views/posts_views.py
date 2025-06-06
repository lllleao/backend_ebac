from rest_framework import viewsets, permissions
from ..models.post_user import Post, Comentario
from ..serializers.posts_serializer import PostSerializer, ComentarioSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all().order_by('-criado_em')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class ComentarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Comentario.objects.all().order_by('-criado_em')
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
