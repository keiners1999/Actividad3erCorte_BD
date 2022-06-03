from django.shortcuts import render, redirect

from apps.usuario.models import Usuario
from apps.usuario.usuarioForm import UsuarioForm

# Create your views here.

def listUsuarios(request):
    usuarios = Usuario.objects.all().order_by('id')
    return render (request, 'usuario/listUsuario.html', {'usuarios':usuarios})

def createUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuarios:listUsuarios') 
    else:
        form = UsuarioForm()
    return render(request, 'usuario/formUsuario.html', {'form': form})

def updateUsuario(request,id):
    usuarios = Usuario.objects.get(id=id)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuarios)
    else:
        form = UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listUsuarios')
    return render(request, 'usuario/formUsuario.html', {'form': form})

def deleteUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios:listUsuarios')