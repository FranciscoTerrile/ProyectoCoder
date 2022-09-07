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
    path('registrar-jugador/', views.crear_jugador, name="jugador_formulario"),
    path('busqueda-jugador-form/', views.buscar_jugador, name="busqueda_jugador_form"),
    path('busqueda-jugador/', views.buscar_jugador, name="busqueda_jugador"),
    path('editar-jugador/<int:id>/', views.editar_jugador, name="editar_jugador"),
    path('eliminar-jugador/<int:id>/', views.eliminar_jugador, name="eliminar_jugador"),
    path('registrar-partido/', views.crear_partido, name="crear_partido"),
    path('busqueda-partido-form/', views.buscar_partido, name="busqueda_partido_form"),
    path('busqueda-partido/', views.buscar_partido, name="busqueda_partido"),
    # URLs de Estudiantes
    path('jugadores/', views.JugadorListView.as_view(), name="jugadores"),
    path('crear-jugador/', views.JugadorCreateView.as_view(), name="crear_jugador"),
    path('editar-jugador/<int:pk>/', views.JugadorUpdateView.as_view(), name="editar_jugador"),
]