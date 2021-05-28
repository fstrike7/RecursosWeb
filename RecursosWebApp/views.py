from typing import List

from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404, redirect 
from RecursosWebApp.models import Categoria, Comentario, Post, Perfil
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, ComentarioForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin, FormView

class HomeView(ListView):
    model = Categoria
    template_name = 'RecursosWebApp/home.html'



class EditarInfoUsuarioView(generic.UpdateView):
    form_class = Perfil
    template_name = "RecursosWebApp/informacion.html"
    success_url = reverse_lazy('editar')

    def get_context_data(self, *args, **kwargs):
        users = Perfil.objects.all()
        context = super(EditarInfoUsuarioView,self).get_context_data(*args, **kwargs)
        context["users"] = users
        return context

class CategoriaView(ListView):
    template_name = "RecursosWebApp/categoria.html"
    
    def get_queryset(self):
        return Post.objects.filter(categorias=self.kwargs['pk'])

class PostView(DetailView):
    model = Post
    template_name ="RecursosWebApp/post_detalle.html"
    form_class = ComentarioForm


class AgregarPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "RecursosWebApp/agregar_post.html"

class AgregarComentarioView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "RecursosWebApp/comentario.html"

    def get_success_url(self):
        return reverse_lazy('post-detallado', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)




class EditarPostView(UpdateView):
    model = Post
    template_name = "RecursosWebApp/actualizar_post.html"
    fields = ['title', 'image', 'categorias','body']

class EliminarPostView(DeleteView):
    model = Post
    template_name = "RecursosWebApp/eliminar_post.html"
    success_url =  reverse_lazy('Inicio')


class EliminarComentarioView(DeleteView):
    model = Comentario
    template_name = "RecursosWebApp/eliminar_comentario.html"
    success_url =  reverse_lazy('Inicio')

def MeGustaView(request, pk):
    post = Post.objects.get(id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detallado', args=[str(pk)]))


def acercade(request):
    return render(request, 'RecursosWebApp/acercade.html')  


class MiembrosView(ListView):
    model = Perfil
    template_name = 'RecursosWebApp/miembros.html'