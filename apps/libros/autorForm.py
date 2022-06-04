from django import forms
from apps.libros.models import Autor

class AutorForm(forms.ModelForm):
    
    class Meta:
        model = Autor
        
        fields = [
            'nombre',
        ]
        
        labels = {
            'nombre': 'Ingrese el nombre del autor',
        }
        
        widges = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
        }