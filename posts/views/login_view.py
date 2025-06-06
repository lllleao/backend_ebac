from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models.user import Usuario

@api_view(['POST'])
def login_usuario(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({"detail": "Usuário e senha são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return Response({"detail": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

    if check_password(password, user.password):
        login(request, user)
        return Response({"detail": "Login realizado com sucesso."}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
