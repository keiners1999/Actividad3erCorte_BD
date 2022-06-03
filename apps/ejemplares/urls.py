from django.urls import path
from apps.ejemplares import views

app_name = 'ejemplares'
urlpatterns = [
    path('', views.listPrestar, name= 'listPrestar'),
    path('createPrestar', views.createPrestar, name= 'createPrestar'),
    path('updatePrestar/<int:i>', views.updatePrestar, name= 'updatePrestar'),
    path('deletePrestar/<int:i>', views.deletePrestar, name= 'deletePrestar'),

    path('listEjemplares', views.listEjemplares, name= 'listEjemplares'),
    path('createEjemplares', views.createEjemplares, name= 'createEjemplares'),
    path('updateEjemplares/<int:i>', views.updateEjemplares, name= 'updateEjemplares'),
    path('deleteEjemplares/<int:i>', views.deleteEjemplares, name= 'deleteEjemplares'),


]
