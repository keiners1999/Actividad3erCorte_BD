
from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    numero_pagina = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)

class Autor(models.Model):
    nombre = models.CharField(max_length=30)


class Escribir(models.Model):
    fecha = models.DateField()
    CodigoAutor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=False, null=False)
    CodigoLibro = models.ForeignKey(Libro, on_delete=models.CASCADE, blank=False, null=False)
