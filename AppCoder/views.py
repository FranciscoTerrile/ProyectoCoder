from datetime import date
from typing import Dict
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from AppCoder.models import Partido, Reserva
from AppCoder.forms import ReservaFormulario


def inicio(request):

      return render(request, "AppCoder/inicio.html")


def partido(request):
      fecha_partido= Partido.objects.all()
      return render(request, "AppCoder/partido.html", {'fecha_partido': fecha_partido})


def jugadores(request):

      return render(request, "AppCoder/jugadores.html")

def reserva(request):
      
      return render(request, "AppCoder/reservas.html")

def reserva_formulario(request):
      if request.method == 'POST':
            formulario= ReservaFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  reservar=Reserva(**data)
                  #reservar = Reserva(nombre=data['nombre'], equipo=data['equipo'])
                  reservar.save()
                  return redirect(reverse('reservas'))
      else:
            formulario= ReservaFormulario()  # Formulario vacio para construir el html
      return render(request, "AppCoder/form_reserva.html", {"formulario": formulario})


def busqueda_reserva(request):
      return render(request, "AppCoder/form_busqueda_reserva.html")


def buscar(request):
      if request.GET["fecha"]:
            nombre = request.GET["nombre"]
            equipo = Reserva.objects.filter(equipo__icontains='equipo')
            return render(request, "AppCoder/reservas.html", {'r': partido})
      else:
            return render(request, "AppCoder/reserva.html", {'reserva': []})

# Create your views here.
