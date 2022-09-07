from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('partido/', views.partido, name="partidos"),
    path('jugadores/', views.jugador, name="jugadores"),
    path('reservas/', views.reservas, name="reservas"),
    path('partidos/', views.partido),
    path('crear-reserva/', views.crear_reserva, name="crear_reserva"),
    path('busqueda-reserva-form/', views.busqueda_reservas, name="busqueda_reserva_form"),
    path('busqueda-reserva/', views.buscar_reserva, name="busqueda_reserva"),
    path('crear-jugador/', views.crear_jugador, name="crear_jugador"),
    path('busqueda-jugador-form/', views.busqueda_jugador, name="busqueda_jugador_form"),
    path('busqueda-jugador/', views.buscar_jugador, name="busqueda_jugador"),
    path('registrar-partido/', views.crear_partido, name="crear_partido"),
    path('busqueda-partido-form/', views.busqueda_partido, name="busqueda_partido_form"),
    path('busqueda-partido/', views.buscar_partido, name="busqueda_partido"),
]