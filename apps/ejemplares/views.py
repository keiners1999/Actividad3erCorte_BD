from django.shortcuts import render, redirect
from apps.ejemplares.ejemplaresForm import EjemplaresForm

from apps.ejemplares.models import Ejemplares, Prestar
from apps.ejemplares.prestarForm import PrestarForm

# Create your views here.

def listPrestar(request):
    prestar = Prestar.objects.all().order_by('id')
    return render (request, 'prestar/listPrestar.html', {'prestar':prestar})

def createPrestar(request):
    if request.method == 'POST':
        form = PrestarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('prestar:listPrestar') 
    else:
        form = PrestarForm()
    return render(request, 'prestar/formPrestar.html', {'form': form})

def updatePrestar(request,id):
    prestar = Prestar.objects.get(id=id)
    if request.method == 'GET':
        form = PrestarForm(instance=prestar)
    else:
        form = PrestarForm(request.POST, instance=prestar)
        if form.is_valid():
            form.save()
            return redirect('prestar:listPrestar')
    return render(request, 'prestar/formPrestar.html', {'form': form})

def deletePrestar(request, id):
    prestar = Prestar.objects.get(id=id)
    prestar.delete()
    return redirect('prestar:listPrestar')


    ################# EJEMPLARES #####################
def listEjemplares(request):
    ejemplares = Ejemplares.objects.all().order_by('id')
    return render (request, 'ejemplares/listEjemplares.html', {'ejemplares':ejemplares})

def createEjemplares(request):
    if request.method == 'POST':
        form = EjemplaresForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listEjemplares') 
    else:
        form = EjemplaresForm()
    return render(request, 'ejemplares/formEjemplares.html', {'form': form})

def updateEjemplares(request,id):
    prestar = Prestar.objects.get(id=id)
    if request.method == 'GET':
        form = PrestarForm(instance=prestar)
    else:
        form = PrestarForm(request.POST, instance=prestar)
        if form.is_valid():
            form.save()
            return redirect('prestar:listPrestar')
    return render(request, 'prestar/formPrestar.html', {'form': form})

def deleteEjemplares(request, id):
    usuario = Prestar.objects.get(id=id)
    usuario.delete()
    return redirect('prestar:listPrestar')