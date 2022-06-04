from django.urls import path
from . import views

app_name = 'libros'
urlpatterns = [
    path('listLibros', views.listLibros, name= 'listLibros'),
    path('createLibro', views.createLibro, name= 'createLibro'),
    path('updateLibro/<int:id>', views.updateLibros, name= 'updateLibro'),
    path('deleteLibro/<int:id>', views.deleteLibros, name= 'deleteLibro'),

]
