from django.db import models


"""
Fanatico (nombre, apellido, email)
Jugador (nombre, apellido, email, pais)
Partido (nombre, fechaDePartido,reservado)
Pais(nombre, jugador_preferido)
"""

class Fanatico(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class Jugador(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    posicion = models.CharField(max_length=128)
    pais = models.CharField(max_length=100)


class Partido(models.Model):
    fecha_de_partido = models.DateField()
    equipo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.equipo} - {self.fecha}'


class Reserva(models.Model):
    nombre = models.CharField(max_length=128)
    reservado = models.BooleanField()
    fecha_de_partido = models.DateField()

# Create your models here.
