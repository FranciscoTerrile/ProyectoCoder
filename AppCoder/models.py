from django.db import models
from django.contrib.auth.models import User

class Jugador(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    posicion = models.CharField(max_length=128)
    pais = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.pais} - {self.posicion}'


class Partido(models.Model):
    fecha = models.DateTimeField() 
    equipo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.equipo} - {self.fecha}'


class Reserva(models.Model):
    nombre = models.CharField(max_length=128)
    fecha = models.DateTimeField()
    equipo = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.equipo} - {self.fecha}'

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"
