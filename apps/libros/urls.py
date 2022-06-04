from django.urls import path
from . import views

app_name = 'libros'
urlpatterns = [
    path('listLibros', views.listLibros, name= 'listLibros'),
    path('createLibro', views.createLibro, name= 'createLibro'),
    path('updateLibro/<int:id>', views.updateLibros, name= 'updateLibro'),
    path('deleteLibro/<int:id>', views.deleteLibros, name= 'deleteLibro'),

    path('listEscribir', views.listEscribir, name= 'listEscribir'),
    path('createLibro', views.createLibro, name= 'createEscribir'),
    path('updateEscribir/<int:id>', views.updateEscribir, name= 'updateEscribir'),
    path('deleteEscribir/<int:id>', views.deleteEscribir, name= 'deleteEscribir'),


]
