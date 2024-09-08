from .models import *
from django import forms 

class FaltasForms(forms.ModelForm):
    class Meta:
        model = Faltas
        fields = ['falta',]
        labels = {
            'falta': 'Selecione o funcionário:'
        }
        
        widgets = {
            'falta': forms.Select(attrs={'class': 'form-select'})
        }