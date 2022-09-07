from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    posicion = models.CharField(max_length=128)
    pais = models.CharField(max_length=100)


class Partido(models.Model):
    fecha = models.DateTimeField() 
    equipo = models.CharField(max_length=100)


class Reserva(models.Model):
    nombre = models.CharField(max_length=128)
    fecha = models.DateTimeField()
    equipo = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.equipo} - {self.fecha}'

# Create your models here.
