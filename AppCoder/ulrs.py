from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('partido/', views.partido, name="partidos"),
    path('jugadores/', views.jugadores, name="jugadores"),
    path('reservas/', views.reserva, name="reservas"),
    path('partidos/', views.partido),
    path('crear-reserva/', views.reserva_formulario, name="reserva_formulario"),
    path('busqueda-partido-form/', views.busqueda_reserva, name="busqueda_reserva_form"),
    path('busqueda-partido/', views.buscar, name="busqueda_reserva"),
    ]
