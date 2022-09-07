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
      
      return render(request, "AppCoder/partido.html")

def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "AppCoder/reservas.html", {'reservas': reservas})

def jugador(request):
      
      return render(request, "AppCoder/jugadores.html")

# Fromulario Reservas

def crear_reserva(request):
    if request.method == 'POST':
        formulario = ReservaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            reserva = Reserva(nombre=data['nombre'], equipo=data['equipo'])
            reserva.save()
            return render(request, "AppCoder/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = ReservaFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_reserva.html", {"formulario": formulario})


def busqueda_reservas(request):
    return render(request, "AppCoder/form_busqueda_reserva.html")


def buscar_reserva(request):
    if request.GET.get['equipo']:
        equipo = request.GET['equipo'] if equipo in request.GET else None
        reservas = Reserva.objects.filter(equipo__icontains=equipo)
        return render(request, "AppCoder/reservas.html", {'reservas': reservas})
    else:
        return render(request, "AppCoder/reservas.html", {'reservas': []})


#Formulario Juagdor
def jugadores(request):
    jugadores = Jugador.objects.all()  # trae todos los jugadores
    contexto = {"jugadores": jugadores}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppCoder/jugadores.html", contexto)


def eliminar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    borrado_id = jugador.id
    jugador.delete()
    url_final = f"{reverse('jugadores')}?borrado={borrado_id}"

    return redirect(url_final)


def crear_jugador(request):
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            jugador = Jugador(**data)
            jugador.save()
            return redirect(reverse('jugadores'))
    else:  # GET
        formulario = JugadorFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_jugador.html", {"formulario": formulario})


def buscar_jugador(request):
    if request.GET["pais"]:
        pais = request.GET["pais"]
        registros = Jugador.objects.filter(pais__icontains=pais)
        return render(request, "AppCoder/jugadores.html", {'registros': registros})
    else:
        return render(request, "AppCoder/jugadores.html", {'registros': []})

def editar_jugador(request, id):
    # Recibe param profesor id, con el que obtenemos el profesor
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
            'email': jugador.posicion,
            'profesion': jugador.pais,
        }
        formulario = JugadorFormulario(initial=inicial)
    return render(request, "AppCoder/form_jugador.html", {"formulario": formulario})


# Vistas de Jugador

class JugadorListView(ListView):
    model = Jugador
    template_name = 'AppCoder/jugadores.html'


class JugadorCreateView(CreateView):
    model = Jugador
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('jugadores')


class JugadorUpdateView(UpdateView):
    model = Jugador
    fields = ['nombre', 'apellido']
    success_url = reverse_lazy('jugadores')


class JugadorDeleteView(DeleteView):
    pass

#Formulario de Partido

def partidos(request):
    partidos = Partido.objects.all()  # trae todos los jugadores
    contexto = {"partidos": partidos}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado

    return render(request, "AppCoder/partido.html", contexto)


def eliminar_partido(request, id):
    partido = Partido.objects.get(id=id)
    borrado_id = partido.id
    partido.delete()
    url_final = f"{reverse('partidos')}?borrado={borrado_id}"

    return redirect(url_final)


def crear_partido(request):
    if request.method == 'POST':
        formulario = PartidoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            partido = Partido(fecha=data['fecha'], equipo=data['equipo'])
            partido.save()
            return redirect(reverse('partidos'))
    else:  # GET
        formulario = PartidoFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCoder/form_partido.html", {"formulario": formulario})


def buscar_partido(request):
    if request.GET["equipo"]:
        equipo = request.GET["equipo"]
        encuentros = Partido.objects.filter(equipo__icontains=equipo)
        return render(request, "AppCoder/partido.html", {'encuentros': encuentros})
    else:
        return render(request, "AppCoder/partido.html", {'encuentros': []})



