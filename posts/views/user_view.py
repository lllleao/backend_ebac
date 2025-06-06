from rest_framework.viewsets import ModelViewSet
from ..models import Usuario
from ..serializers import UsuarioSignupSerializer

class UserView(ModelViewSet):
    serializer_class = UsuarioSignupSerializer

    def get_queryset(self):
        return Usuario.objects.all().order_by("id")
