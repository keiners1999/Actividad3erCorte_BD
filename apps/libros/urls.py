from django.urls import path
from . import views

app_name = 'libros'
urlpatterns = [
    path('listLibros', views.listLibros, name= 'listLibros'),
    path('createLibro', views.createLibro, name= 'createLibro'),
    path('updateLibro/<int:id>', views.updateLibros, name= 'updateLibro'),
    path('deleteLibro/<int:id>', views.deleteLibros, name= 'deleteLibro'),

    ##########ESCRIBIR#################
    path('listEscribir', views.listEscribir, name= 'listEscribir'),
    path('createLibro', views.createLibro, name= 'createEscribir'),
    path('updateEscribir/<int:id>', views.updateEscribir, name= 'updateEscribir'),
    path('deleteEscribir/<int:id>', views.deleteEscribir, name= 'deleteEscribir'),

    ###########AUTOR########################
    path('listAutor', views.listAutor, name= 'listAutor'),
    path('createAutor', views.createAutor, name= 'createAutor'),
    path('updateAutor/<int:id>', views.updateAutor, name= 'updateAutor'),
    path('deleteAutor/<int:id>', views.deleteAutor, name= 'deleteAutor'),


]
