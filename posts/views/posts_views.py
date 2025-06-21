from rest_framework import viewsets, permissions
from ..models.post_user import Post, Comentario
from ..serializers.posts_serializer import PostSerializer, ComentarioSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-criado_em')

        user_id = self.request.query_params.get('user_id')
        if user_id:
            return queryset.filter(autor_id=user_id)

        excluir_user = self.request.query_params.get('exclude_user')
        if excluir_user == 'me' and self.request.user.is_authenticated:
            return queryset.exclude(autor=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class ComentarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        queryset = Comentario.objects.all().order_by('-criado_em')
        post_id = self.request.query_params.get('post')
        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
