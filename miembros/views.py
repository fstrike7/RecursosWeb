from RecursosWebApp.models import Perfil
from miembros.forms import RegistrarseForm
from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditarPerfilForm, RegistrarseForm, CambiarPassForm
from RecursosWebApp.forms import PerfilForm

class PasswordsChangeView(PasswordChangeView):
    form_class = CambiarPassForm
    success_url = reverse_lazy('cambiar-pass-success')

class RegistroUsuarioView(generic.CreateView):
    form_class = RegistrarseForm
    template_name = "registration/registro.html"
    success_url = reverse_lazy('login')

class EditarUsuarioView(generic.UpdateView):
    form_class = EditarPerfilForm
    template_name = "registration/privacidad.html"
    success_url = reverse_lazy('editar')

    def get_object(self):
        return self.request.user

class EditarInfoUsuarioView(generic.UpdateView):
    model = Perfil
    template_name = 'registration/informacion.html'
    fields = ['bio', 'profile_pic', 'webpage', 'numero']
    success_url = reverse_lazy('Inicio')

def password_success(request):
    return render(request, 'registration/pass_success.html', {})