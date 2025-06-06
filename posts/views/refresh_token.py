from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        print(refresh_token)

        if not refresh_token:
            raise AuthenticationFailed("Refresh token não encontrado.")

        try:
            refresh = RefreshToken(refresh_token)
            data = {
                "access": str(refresh.access_token)
            }
            return Response(data)
        except Exception as e:
            raise AuthenticationFailed("Token inválido ou expirado.")
