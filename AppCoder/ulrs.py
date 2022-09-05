from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('partido/', views.partido, name="partidos"),
    path('jugadores/', views.jugadores, name="jugadores"),
    path('fanaticos/', views.reservas, name="reservas"),
    path('partidos/', views.partido),
    path('crear-reserva/', views.reserva_formulario, name="partido_formulario"),
    path('busqueda-partido-form/', views.busqueda_pais, name="busqueda_partido_form"),
    path('busqueda-partido/', views.buscar, name="busqueda_partido"),
    ]
