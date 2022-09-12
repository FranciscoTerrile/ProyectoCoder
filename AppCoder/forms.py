#from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    fecha = forms.DateTimeField() 
    equipo = forms.CharField(max_length=100)
    email = forms.EmailField() 
class JugadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    posicion = forms.CharField(max_length=128)
    pais = forms.CharField(max_length=100)

class PartidoFormulario(forms.Form):
    fecha = forms.DateTimeField() 
    equipo = forms.CharField(max_length=100)

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']