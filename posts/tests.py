from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class UsuarioSignupTestCase(APITestCase):
    def test_criacao_de_usuario(self):
        url = reverse('users-list')  # ou o nome que você colocou nas rotas
        data = {
            "username": "testeuser",
            "email": "teste@example.com",
            "password": "senhasegura123",
            "complet_name": "Usuário Teste"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Usuario.objects.filter(email="teste@example.com").exists())

        usuario = Usuario.objects.get(email="teste@example.com")
        self.assertNotEqual(usuario.password, data["password"])  # Senha deve estar criptografada
