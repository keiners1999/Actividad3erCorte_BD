from django import forms
from apps.ejemplares.models import Prestar

class PrestarForm(forms.ModelForm):
    
    class Meta:
        model = Prestar
        
        fields = [
            'Usuario',
            'Ejemplar',
            'fechaDevolucion',
            'fechaPrestamo',
        ]
        
        labels = {
            'Usuario': 'Ingrese el usuario',
            'Ejemplar': 'Ingrese el ejemplar',
            'fechaDevolucion': 'Ingrese la fecha de devolución',
            'fechaPrestamo': 'Ingrese la fecha de prestamo',
        }
        
        widges = {
            'Usuario' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'Ejemplar' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fechaDevolucion' : forms.DateField(),
            'fechaPrestamo' : forms.DateField(),
        }