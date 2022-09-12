# from datetime import date
# from typing import Dict
# from django.shortcuts import HttpResponse
#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from AppCoder.models import Partido, Reserva, Jugador
from AppCoder.forms import ReservaFormulario, JugadorFormulario, PartidoFormulario, UserRegisterForm
from django.urls import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView

@login_required
def inicio(request):

      return render(request, "AppCoder/inicio.html")

@login_required
def partido(request):
    partidos = Partido.objects.all()
    return render(request, "AppCoder/partido.html", {'partidos': partidos})

@login_required
def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "AppCoder/reservas.html", {'reservas': reservas})

@login_required
def jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, "AppCoder/jugadores.html", {'jugadores': jugadores})

# Formulario Reservas

@login_required
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

@login_required
def busqueda_reservas(request):
    return render(request, "AppCoder/form_busqueda_reserva.html")

@login_required
def buscar_reserva(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre'] #if nombre in request.GET else None
        reservas = Reserva.objects.filter(nombre__icontains=nombre)
        return render(request, "AppCoder/reservas.html", {'reservas': reservas})
    else:
        return render(request, "AppCoder/reservas.html", {'reservas': []})

@login_required
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

@login_required
def eliminar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    borrado_id = reserva.id
    reserva.delete()
    url_final = f"{reverse('reservas')}?borrado={borrado_id}"

    return redirect(url_final)
    
#Formulario Juagdor

@login_required
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

@login_required
def busqueda_jugador(request):
    return render(request, "AppCoder/form_busqueda_jugador.html")

@login_required
def buscar_jugador(request):
    if request.GET['pais']:
        pais = request.GET['pais'] 
        jugadores = Jugador.objects.filter(pais__icontains=pais)
        return render(request, "AppCoder/jugadores.html", {'jugadores': jugadores})
    else:
        return render(request, "AppCoder/jugadores.html", {'jugadores': []})

@login_required
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

@login_required
def eliminar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    borrado_id = jugador.id
    jugador.delete()
    url_final = f"{reverse('jugadores')}?borrado={borrado_id}"

    return redirect(url_final)

#Formulario de Partido

@login_required
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

@login_required
def busqueda_partido(request):
    return render(request, "AppCoder/form_busqueda_partido.html")

@login_required
def buscar_partido(request):
    if request.GET['equipo']:
        equipo = request.GET['equipo']
        partidos = Partido.objects.filter(equipo__icontains=equipo)
        return render(request, "AppCoder/partido.html", {'partidos': partidos})
    else:
        return render(request, "AppCoder/partido.html", {'partidos': []})

@login_required
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

@login_required
def eliminar_partido(request, id):
    partido = Partido.objects.get(id=id)
    borrado_id = partido.id
    partido.delete()
    url_final = f"{reverse('partidos')}?borrado={borrado_id}"

    return redirect(url_final)

# Views de usuarios, registro, login o logout

def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado con exito :"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }
    return render(request, "AppCoder/registro.html", context=context)

def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"AppCoder/login.html", {'form':form} )

class CustomLogoutView(LogoutView):
    template_name = 'AppCoder/logout.html'

