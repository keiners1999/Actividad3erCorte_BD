from django.db import models

from apps.libros.models import Libro
from apps.usuario.models import Usuario

# Create your models here.

class Ejemplares(models.Model):
    CodigoLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    localizacion = models.CharField(max_length=30)

    def __str__(self):
        return self.CodigoLibro
    

class Prestar(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Ejemplar = models.ForeignKey(Ejemplares, on_delete=models.CASCADE)
    fechaDevolucion = models.DateField()
    fechaPrestamo = models.DateField()

    