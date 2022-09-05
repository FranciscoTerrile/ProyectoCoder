from django import forms

class ReservaFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    reservado = forms.BooleanField()
    fecha_de_partido = forms.DateField()
    equipo = forms.CharField(max_length=100)
    email = forms.EmailField()