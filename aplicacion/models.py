from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Categoría
class Categoria(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Mecánica
class Mecanica(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField()  

    def __str__(self):
        return self.nombre

# Juegos
class Juego(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    imagen = models.ImageField(upload_to='juegos_imagenes/')
    editorial = models.CharField(max_length=100)
    jugadores = models.CharField(max_length=100)
    mecanica = models.ManyToManyField(Mecanica, blank=True)  
    categoria = models.ManyToManyField(Categoria, blank=True)  
    duracion = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Usuario
class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to="fotos_perfil/", null=True, blank=True)
    email = models.EmailField(unique=True, max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    mis_juegos = models.ManyToManyField(Juego, blank=True, related_name='usuarios')  

    def __str__(self):
        return self.username
    
#prestamo
class Prestamo(models.Model):
    usuario_presta = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestamos_usuario_presta')
    usuario_pide = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='prestamos_usuario_pide')
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='prestamos_juego') #no me deja poner el mismo related_name porque da conflicto
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.usuario_presta, self.usuario_pide, self.juego}'