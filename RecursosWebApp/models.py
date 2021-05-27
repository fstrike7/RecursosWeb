from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    title=models.CharField(max_length=25)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='categorias', null=True, blank=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(verbose_name='Título',max_length=255)
    author = models.ForeignKey(verbose_name='Autor',to=User, on_delete = models.CASCADE)
    body = RichTextField(blank=True, null=True)
    categorias = models.ManyToManyField(verbose_name='Categoria',to=Categoria)
    image=models.ImageField(verbose_name='Imagen',upload_to='posts', default="/posts/200.gif")
    likes = models.ManyToManyField(User, related_name='blog_post')
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post-detallado', args=[str(self.id)] )

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Biografía", blank=True, null=True)
    profile_pic = models.ImageField(verbose_name='Foto de perfil',upload_to='profile_pics', default="/profile_pics/profile-default.svg")
    webpage = models.CharField(verbose_name='Sitio Web',max_length=255, null=True, blank=True)
    numero = models.CharField(verbose_name='WhatsApp',max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="usuarios", on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Contenido')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='comentario'
        verbose_name_plural='comentarios'
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.user.username)
    
    
    def get_absolute_url(self):
        return reverse('post-detallado', args=[str(self.post.id)] )