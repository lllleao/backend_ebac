from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Usuario
from ..serializers import UsuarioSignupSerializer

class UserView(ModelViewSet):
    serializer_class = UsuarioSignupSerializer
    queryset = Usuario.objects.all().order_by("id")

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
