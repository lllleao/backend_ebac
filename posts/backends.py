from django.contrib.auth.backends import ModelBackend
from .models.user import Usuario

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuario.objects.get(email=username)
            if user.check_password(password):
                return user
        except Usuario.DoesNotExist:
            return None
