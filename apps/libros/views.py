from django.shortcuts import render, redirect

from apps.libros.models import Libro
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