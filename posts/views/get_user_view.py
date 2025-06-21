from rest_framework.views import APIView
from ..serializers.get_user_serializer import GetUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class GetUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = GetUserSerializer(user)
        return Response(serializer.data)
