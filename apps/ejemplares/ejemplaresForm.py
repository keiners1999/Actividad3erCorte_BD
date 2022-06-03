from django import forms
from apps.ejemplares.models import Ejemplares

class EjemplaresForm(forms.ModelForm):
    
    class Meta:
        model = Ejemplares
        
        fields = [
            'CodigoLibro',
            'localizacion',
        ]
        
        labels = {
            'CodigoLibro': 'Ingrese el libro',
            'localizacion': 'Ingrese la localización',
        }
        
        widges = {
            'CodigoLibro' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'localizacion' : forms.TextInput(attrs={'class': 'form-control'}),
        }