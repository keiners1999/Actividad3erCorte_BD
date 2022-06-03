from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    