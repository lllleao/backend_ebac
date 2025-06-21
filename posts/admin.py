from django.contrib import admin

# Register your models here.
from .models.user import Usuario
from .models.post_user import Comentario, Post

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'username', 'is_staff', 'complet_name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'autor', 'conteudo', 'criado_em']
    search_fields = ['conteudo']
    list_filter = ['criado_em']
    # autocomplete_fields = ['autor']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'autor', 'texto', 'criado_em']
    search_fields = ['texto']
    list_filter = ['criado_em']
