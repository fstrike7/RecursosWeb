from RecursosWebApp.forms import PerfilForm
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from RecursosWebApp.models import Perfil

class RegistrarseForm(UserCreationForm):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Nombre",max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Apellido",max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        context = super(RegistrarseForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = "Nombre de usuario"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = "Contraseña"

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = "Confirmar contraseña"


class EditarPerfilForm(UserChangeForm):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Nombre",max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Apellido",max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Nombre de usuario",max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class CambiarPassForm(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña actual", widget=forms.PasswordInput(attrs={"class":"form-control", 'type':'password'}))
    new_password1 = forms.CharField(label="Contraseña nueva",max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control",'type':'password'}))
    new_password2 = forms.CharField(label="Confirmar contraseña nueva",max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control",'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')