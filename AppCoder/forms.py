from django import forms


class PartidoFormulario(forms.Form):
    fecha = forms.DateField()
    equipo = forms.CharField(max_length=100)