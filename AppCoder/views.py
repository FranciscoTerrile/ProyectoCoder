from datetime import date
from typing import Dict
from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Partido, Reserva
from AppCoder.forms import PartidoFormulario


def inicio(request):

      return render(request, "AppCoder/inicio.html")


def partido(request):
      fecha_partido= Partido.objects.all()
      return render(request, "AppCoder/partido.html", {'fecha_partido': fecha_partido})


def jugadores(request):

      return render(request, "AppCoder/jugadores.html")


def reservas(request):

      return render(request, "AppCoder/reservas.html")


def partidos(request):

      return render(request, "AppCoder/partidos.html")

def reserva_formulario(request):
      if request.method == "POST":
            data_formulario: Dict = request.POST
            Partidos = Partido(pais=data_formulario['pais'], dni=data_formulario['dni'])
            Partidos.save()
            return render (request, "AppCoder/inicio.html")
      else:
            return render(request,"AppCoder/form:pais.html")

def reserva_formulario(request):
      if request.method == 'POST':
            formulario= PartidoFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  Reservar = Partido(equipo=data['equipo'], fecha=date['fecha'])
                  Reservar.save()
                  return render(request, "AppCoder/inicio.html", {"exitoso": True})
      else:
            return render(request, "AppCoder/form_partido.html")

            formulario= IdFormulario()  # Formulario vacio para construir el html
      return render(request, "AppCoder/form_partido.html", {"formulario": formulario})


def busqueda_pais(request):
      return render(request, "AppCoder/form_busqueda_pais.html")


def buscar(request):
      if request.GET["fecha"]:
            equipo_fecha = request.GET["partido_fecha"]
            equipo_fecha = Partido.objects.filter(equipo__icontains='equipo')
            return render(request, "AppCoder/partido.html", {'r': partido})
      else:
            return render(request, "AppCoder/reserva.html", {'reserva': []})

# Create your views here.
