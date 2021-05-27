from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', views.HomeView, name="Inicio"),
    path('', HomeView.as_view(), name="Inicio"),
    path('acercade', views.acercade, name="Acerca"),
    path('categoria/<int:pk>/', CategoriaView.as_view(), name="filtro-categoria"),
    path('post/<int:pk>', PostView.as_view(), name="post-detallado"),
    path('agregar_post/', AgregarPostView.as_view(), name="Agregar-Post"),
    path('post/editar/<int:pk>', EditarPostView.as_view(), name="Editar-Post"),
    path('post/<int:pk>/eliminar', EliminarPostView.as_view(), name="Eliminar-Post"),
    path('like/<int:pk>', MeGustaView, name="like_post"),
    path('post/<int:pk>/comentario/', AgregarComentarioView.as_view(), name="Agregar-Comentario"),
    path('post/<int:pk>/comentario/eliminar', EliminarComentarioView.as_view(), name="Eliminar-Comentario"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)