from django import forms
from apps.ejemplares.models import Prestar

class PrestarForm(forms.ModelForm):
    
    class Meta:
        model = Prestar
        
        fields = [
            'Usuario',
            'Ejemplar',
            'fechaPrestamo',
            'fechaDevolucion',
        ]
        
        labels = {
            'Usuario': 'Ingrese el usuario',
            'Ejemplar': 'Ingrese el ejemplar',
            'fechaPrestamo': 'Ingrese la fecha de prestamo',
            'fechaDevolucion': 'Ingrese la fecha de devolución',
        }
        
        widges = {
            'Usuario' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'Ejemplar' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fechaPrestamo' : forms.DateField(),
            'fechaDevolucion' : forms.DateField(),
        }