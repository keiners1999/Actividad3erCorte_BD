from django import forms
from apps.libros.models import Escribir

class EscribirForm(forms.ModelForm):
    
    class Meta:
        model = Escribir
        
        fields = [
            'fecha',
            'CodigoAutor',
            'CodigoLibro',
        ]
        
        labels = {
            'fecha': 'Ingrese la fecha',
            'CodigoAutor': 'Ingrese el Autor',
            'CodigoLibro': 'Ingrese el libro',   
        }
        
        widges = {
            'fecha' : forms.DateField(),
            'CodigoAutor' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'CodigoLibro' : forms.SelectMultiple(attrs={'class': 'form-control'}),
        }