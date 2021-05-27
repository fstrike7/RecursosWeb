from django import forms
from django.forms import widgets
from .models import Categoria, Comentario, Perfil, Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'categorias', 'image', 'body')

        #choices = Categoria.objects.all().values_list('title', 'title')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'formulario-control titulo'} ),
            'author' : forms.TextInput(attrs={'class':'formulario-control autor', 'value':'', 'id':'username', 'type':'hidden'}),
            #'categorias' : forms.SelectMultiple(choices=choices, attrs=({'class':'selector'})),
            'image' : forms.ImageField().widget.attrs.update({'class':'selector'}),
            'body' : forms.Textarea(attrs={'class':'formulario-control cuerpo'} )
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('profile_pic','bio', 'webpage', 'numero')
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'formulario-control titulo'} ),
            'webpage' : forms.URLInput(attrs={'class':'formulario-control titulo'} ),
            'profile_pic' : forms.ImageField().widget.attrs.update({'class':'selector imagen'}),
            'body' : forms.Textarea(attrs={'class':'formulario-control cuerpo'} )
        }

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('body',)
        
        widgets = {
            'body' : forms.Textarea(attrs={'class':'formulario-control comentario'} ),
        }