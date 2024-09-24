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
        
class AtrasosForms(forms.ModelForm):
    class Meta:
        model = Atrasos
        fields = ['funcionarios','atraso']
        labels = {
            'funcionario': 'Selecione o funcionário:',
            'atraso': 'Digite o tempo de atraso:'
        }
        
        widgets = {
            'funcionarios': forms.Select(attrs={'class': 'form-select p-2'}),
            'atraso': forms.TextInput(attrs={'class': 'form-control p-2'})
        }