from django.urls import include, path

from posts.views.updata_bio_views import UpdateBioView
from .views.user_view import UserView
from .views.login_view import login_usuario
from rest_framework import routers
from .views.token_views import CustomTokenObtainPairView
from .views.refresh_token import RefreshTokenView
from .views.get_user_view import GetUserView
from .views.followers_view import FollowersView
from .views.posts_views import PostViewSet, ComentarioViewSet
from rest_framework_simplejwt.views import TokenBlacklistView
from .views.avatar_views import AtualizarAvatarView

router = routers.SimpleRouter()
router.register(r'users', UserView, basename='users')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comentarios', ComentarioViewSet, basename='comentarios')

urlpatterns = [
    path('', include(router.urls)),
    path('login', login_usuario, name='login'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('user_data/', GetUserView.as_view(), name='user_data'),
    path('update_bio/', UpdateBioView.as_view(), name='update_bio'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('follow/', FollowersView.as_view(), name='follow'),
    path('avatar/', AtualizarAvatarView.as_view(), name='atualizar_avatar'),
]
