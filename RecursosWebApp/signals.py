from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender=User)
def post_create_profile(sender, instance, created, **kwargs):
    if created: # Si la creación del usuario es TRUE
        print('Creando perfil.')
        Perfil.objects.create(user=instance) # Manda la instancia "usuario" como el atributo "user" de mi modelo Perfil.