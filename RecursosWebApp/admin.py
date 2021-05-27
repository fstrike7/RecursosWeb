from django.contrib import admin

from .models import Post, Categoria, Perfil, Comentario

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Perfil)
admin.site.register(Comentario)

# Register your models here.
