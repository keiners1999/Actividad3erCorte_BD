from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.listUsuarios, name= 'listUsuarios'),
    path('createUsuario', views.createUsuario, name= 'createUsuario'),
    path('updateUsuario/<int:id>', views.updateUsuario, name= 'updateUsuario'),
    path('deleteUsuario/<int:id>', views.deleteUsuario, name= 'deleteUsuario'),

]
