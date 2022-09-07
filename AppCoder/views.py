from datetime import date
from typing import Dict
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from AppCoder.models import Partido, Reserva, Jugador
from AppCoder.forms import ReservaFormulario, JugadorFormulario, PartidoFormulario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def partido(request):
    partidos = Partido.objects.all()
    return render(request, "AppCoder/partido.html", {'partidos': partidos})
      

def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "AppCoder/reservas.html", {'reservas': reservas})

def jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, "AppCoder/jugadores.html", {'jugadores': jugadores})

# Fromulario Reservas

def crear_reserva(request):
    if request.method == 'POST':
        formulario = ReservaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            reserva = Reserva(**data)
            reserva.save()
            return render(request, "AppCoder/inicio.html", {"exitoso": True})
    else:  
        formulario = ReservaFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_reserva.html", {"formulario": formulario})


def busqueda_reservas(request):
    return render(request, "AppCoder/form_busqueda_reserva.html")


def buscar_reserva(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre'] #if nombre in request.GET else None
        reservas = Reserva.objects.filter(nombre__icontains=nombre)
        return render(request, "AppCoder/reservas.html", {'reservas': reservas})
    else:
        return render(request, "AppCoder/reservas.html", {'reservas': []})

#Formulario Juagdor

def crear_jugador(request):
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            jugador = Jugador(**data)
            jugador.save()
            return render(request, "AppCoder/inicio.html", {"exitoso1": True})
    else:  # GET
        formulario = JugadorFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_jugador.html", {"formulario": formulario})

def busqueda_jugador(request):
    return render(request, "AppCoder/form_busqueda_jugador.html")


def buscar_jugador(request):
    if request.GET['pais']:
        pais = request.GET['pais'] 
        jugadores = Jugador.objects.filter(pais__icontains=pais)
        return render(request, "AppCoder/jugadores.html", {'jugadores': jugadores})
    else:
        return render(request, "AppCoder/jugadores.html", {'jugadores': []})

#Formulario de Partido

def crear_partido(request):
    if request.method == 'POST':
        formulario = PartidoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            partido = Partido(**data)
            partido.save()
            return render(request, "AppCoder/inicio.html", {"exitoso2": True})
    else:  
        formulario = PartidoFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_partido.html", {"formulario": formulario})

    
def busqueda_partido(request):
    return render(request, "AppCoder/form_busqueda_partido.html")

def buscar_partido(request):
    if request.GET['equipo']:
        equipo = request.GET['equipo']
        partidos = Partido.objects.filter(equipo__icontains=equipo)
        return render(request, "AppCoder/partido.html", {'partidos': partidos})
    else:
        return render(request, "AppCoder/partido.html", {'partidos': []})



