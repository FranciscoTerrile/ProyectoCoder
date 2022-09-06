from datetime import date
from typing import Dict
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from AppCoder.models import Partido, Reserva, Jugador
from AppCoder.forms import ReservaFormulario,JugadorFormulario


def inicio(request):

      return render(request, "AppCoder/inicio.html")


def partido(request):
      fecha_partido= Partido.objects.all()
      return render(request, "AppCoder/partido.html", {'fecha_partido': fecha_partido})


def jugadores(request):

      return render(request, "AppCoder/jugadores.html")

def reserva(request):
      
      return render(request, "AppCoder/reservas.html")

# Fromulario Reservas

def reserva_formulario(request):
      if request.method == 'POST':
            formulario= ReservaFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  reservar=Reserva(**data)
                  reservar = Reserva(nombre=data['nombre'], equipo=data['equipo'])
                  reservar.save()
                  return redirect(reverse('reservas'))
      else:
            formulario= ReservaFormulario()  # Formulario vacio para construir el html
      return render(request, "AppCoder/form_reserva.html", {"formulario": formulario})


def busqueda_reserva(request):
      return render(request, "AppCoder/form_busqueda_reserva.html")


def buscar_reserva(request):
      if request.GET["equipo"]:
            equipo = request.GET["equipo"]
            reservas = Reserva.objects.filter(equipo__icontains= equipo)
            return render(request, "AppCoder/reservas.html", {'reserva': reservas})
      else:
            return render(request, "AppCoder/reservas.html", {'reserva': []})

#Formulario Juagdor
def jugador_formulario(request):
      if request.method == 'POST':
            formulario= JugadorFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  registrar=Jugador(**data)
                  registrar = Jugador(nombre=data['nombre'], pais=data['pais'])
                  registrar.save()
                  return redirect(reverse('jugadores'))
      else:
            formulario= JugadorFormulario()  # Formulario vacio para construir el html
      return render(request, "AppCoder/form_jugador.html", {"formulario": formulario})

def busqueda_jugador(request):
      return render(request, "AppCoder/form_busqueda_jugador.html")

def buscar_jugador(request):
      if request.GET["fecha"]:
            nombre = request.GET["nombre"]
            equipo = Reserva.objects.filter(equipo__icontains='pais')
            return render(request, "AppCoder/jugadores.html", {'r': partido})
      else:
            return render(request, "AppCoder/jugadores.html", {'nombre': []})
