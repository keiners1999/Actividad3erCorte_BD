from django.shortcuts import render, redirect
from apps.libros.escribirForm import EscribirForm

from apps.libros.models import Escribir, Libro
from apps.libros.librosForm import LibrosForm

# Create your views here.

def listLibros(request):
    libros = Libro.objects.all().order_by('id')
    return render (request, 'libro/listLibros.html', {'libros':libros})

def createLibro(request):
    if request.method == 'POST':
        form = LibrosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libros:listLibros') 
    else:
        form = LibrosForm()
    return render(request, 'libro/formLibros.html', {'form': form})

def updateLibros(request,id):
    libros = Libro.objects.get(id=id)
    if request.method == 'GET':
        form = LibrosForm(instance=libros)
    else:
        form = LibrosForm(request.POST, instance=libros)
        if form.is_valid():
            form.save()
            return redirect('libros:listLibros')
    return render(request, 'libros/formLibros.html', {'form': form})

def deleteLibros(request, id):
    libros = Libro.objects.get(id=id)
    libros.delete()
    return redirect('libros:listLibros')

#########################ESCRIBIR###########################
def listEscribir(request):
    escribir = Escribir.objects.all().order_by('id')
    return render (request, 'escribir/listEscribir.html', {'escribir':escribir})

def createEscribir(request):
    if request.method == 'POST':
        form = EscribirForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('escribir:listEscribir') 
    else:
        form = EscribirForm()
    return render(request, 'libro/formEscribir.html', {'form': form})

def updateEscribir(request,id):
    escribir = Escribir.objects.get(id=id)
    if request.method == 'GET':
        form = EscribirForm(instance=escribir)
    else:
        form = EscribirForm(request.POST, instance=escribir)
        if form.is_valid():
            form.save()
            return redirect('escribir:listEscribir')
    return render(request, 'escribir/formEscribir.html', {'form': form})

def deleteEscribir(request, id):
    escribir = Escribir.objects.get(id=id)
    escribir.delete()
    return redirect('escribir:listEscribir')