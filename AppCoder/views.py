from datetime import date
from typing import Dict
from django.shortcuts import render, HttpResponse
from django.shortcuts import render
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
      if request.method == "POST":
            data_formulario: Dict = request.POST
            Reservas = Reserva(nombre=data_formulario['nombre'], equipo=data_formulario['equipo'])
            Reservas.save()
            return render (request, "AppCoder/inicio.html")
      else:
            return render(request,"AppCoder/form:reservas.html")

def reserva_formulario(request):
      if request.method == 'POST':
            formulario= ReservaFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  Reservar = Reserva(nombre=data['nombre'], equipo=data['equipo'])
                  Reservar.save()
                  return render(request, "AppCoder/inicio.html", {"exitoso": True})
      else:
            return render(request, "AppCoder/form_reserva.html")

            formulario= IdFormulario()  # Formulario vacio para construir el html
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
