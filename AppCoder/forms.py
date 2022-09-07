from django import forms

class ReservaFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    fecha = forms.DateField() 
    equipo = forms.CharField(max_length=100)
    email = forms.EmailField()

class JugadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    posicion = forms.CharField(max_length=128)
    pais = forms.CharField(max_length=100)

class PartidoFormulario(forms.Form):
    fecha = forms.DateField() 
    equipo = forms.CharField(max_length=100)