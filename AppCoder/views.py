from datetime import date
from typing import Dict
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Partido, Reserva, Jugador
from AppCoder.forms import ReservaFormulario, JugadorFormulario, PartidoFormulario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


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

# Formulario Reservas

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

def editar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)

    if request.method == 'POST':
        formulario = ReservaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            reserva.nombre = data['nombre']
            reserva.fecha = data['fecha']
            reserva.equipo = data['equipo']
            reserva.email = data['email']

            reserva.save()

            return redirect(reverse('reservas'))
    else:  # GET
        inicial = {
            'nombre': reserva.nombre,
            'fecha': reserva.fecha,
            'equipo': reserva.equipo,
            'email': reserva.email,            
        }
        formulario = ReservaFormulario(initial=inicial)
    return render(request, "AppCoder/form_reserva.html", {"formulario": formulario})

def eliminar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    borrado_id = reserva.id
    reserva.delete()
    url_final = f"{reverse('reservas')}?borrado={borrado_id}"

    return redirect(url_final)
    

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

def editar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)

    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            jugador.nombre = data['nombre']
            jugador.apellido = data['apellido']
            jugador.posicion = data['posicion']
            jugador.pais = data['pais']

            jugador.save()

            return redirect(reverse('jugadores'))
    else:  # GET
        inicial = {
            'nombre': jugador.nombre,
            'apellido': jugador.apellido,
            'posicion': jugador.posicion,
            'pais': jugador.pais,
        }
        formulario = JugadorFormulario(initial=inicial)
    return render(request, "AppCoder/form_jugador.html", {"formulario": formulario})

def eliminar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    borrado_id = jugador.id
    jugador.delete()
    url_final = f"{reverse('jugadores')}?borrado={borrado_id}"

    return redirect(url_final)


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

def editar_partido(request, id):
    partido = Partido.objects.get(id=id)

    if request.method == 'POST':
        formulario = PartidoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            partido.fecha = data['fecha']
            partido.equipo = data['equipo']

            partido.save()

            return redirect(reverse('partidos'))
    else:  # GET
        inicial = {
            'fecha': partido.fecha,
            'equipo': partido.equipo,
        }
        formulario = PartidoFormulario(initial=inicial)
    return render(request, "AppCoder/form_partido.html", {"formulario": formulario})

def eliminar_partido(request, id):
    partido = Partido.objects.get(id=id)
    borrado_id = partido.id
    partido.delete()
    url_final = f"{reverse('partidos')}?borrado={borrado_id}"

    return redirect(url_final)


