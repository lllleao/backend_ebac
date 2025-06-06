from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..serializers.avatar_serializer import AvatarSerializer

class AtualizarAvatarView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        print(request.data.get('formData'))
        serializer = AvatarSerializer(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        avatar_url = request.user.avatar.url if request.user.avatar else None
        absolute_url = request.build_absolute_uri(avatar_url) if avatar_url else None

        return Response({
            "message": "Avatar atualizado com sucesso.",
            "avatar_url": absolute_url
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        avatar_url = request.user.avatar.url if request.user.avatar else None
        print(avatar_url)
        return Response({
            "avatar_url": request.build_absolute_uri(avatar_url) if avatar_url else None
        })
