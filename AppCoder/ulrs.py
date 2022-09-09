from django.urls import path

from AppCoder import views

urlpatterns = [
    #Barra inicial
    path('', views.inicio, name="inicio"),
    path('partido/', views.partido, name="partidos"),
    path('jugadores/', views.jugador, name="jugadores"),
    path('reservas/', views.reservas, name="reservas"),
    #Reservas
    path('crear-reserva/', views.crear_reserva, name="crear_reserva"),
    path('busqueda-reserva-form/', views.busqueda_reservas, name="busqueda_reserva_form"),
    path('busqueda-reserva/', views.buscar_reserva, name="busqueda_reserva"),
    path('editar-reserva/<int:id>/', views.editar_reserva, name="editar_reserva"),
    path('eliminar-reserva/<int:id>/', views.eliminar_reserva, name="eliminar_reserva"),
    #Jugadores
    path('crear-jugador/', views.crear_jugador, name="crear_jugador"),
    path('busqueda-jugador-form/', views.busqueda_jugador, name="busqueda_jugador_form"),
    path('busqueda-jugador/', views.buscar_jugador, name="busqueda_jugador"),
    path('editar-jugador/<int:id>/', views.editar_jugador, name="editar_jugador"),
    path('eliminar-jugador/<int:id>/', views.eliminar_jugador, name="eliminar_jugador"),
    path('registrar-partido/', views.crear_partido, name="crear_partido"),
    #Partidos
    path('busqueda-partido-form/', views.busqueda_partido, name="busqueda_partido_form"),
    path('busqueda-partido/', views.buscar_partido, name="busqueda_partido"),
    path('editar-partido/<int:id>/', views.editar_partido, name="editar_partido"),
    path('eliminar-partido/<int:id>/', views.eliminar_partido, name="eliminar_partido"),
]