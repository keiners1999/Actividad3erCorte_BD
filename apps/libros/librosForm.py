from django import forms
from apps.libros.models import Libro

class LibrosForm(forms.ModelForm):
    
    class Meta:
        model = Libro
        
        fields = [
            'titulo',
            'numero_pagina',
            'editorial',
            'isbn',
        ]
        
        labels = {
            'titulo': 'Ingrese el Titulo',
            'numero_pagina': 'Ingrese el numero de paginas',
            'editorial': 'Ingrese el editorial',
            'isbn': 'Ingrese el isbn',
        }
        
        widges = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'numero_pagina' : forms.TextInput(attrs={'class': 'form-control'}),
            'editorial' : forms.TextInput(attrs={'class': 'form-control'}),
            'isbn' : forms.TextInput(attrs={'class': 'form-control'}),
        }