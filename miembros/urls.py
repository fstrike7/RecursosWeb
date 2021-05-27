from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrarse/', RegistroUsuarioView.as_view(), name="registrarse"),
    path('editar_perfil/', EditarUsuarioView.as_view(), name="editar"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/cambiar-pass.html')),
    path('password_success/', password_success, name="cambiar-pass-success"),
    path('<int:pk>/editar_info/', EditarInfoUsuarioView.as_view(), name="editar_info"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)