from django import forms
from .models import *

class FuncionariosForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'CPF', 'endereco', 'telefone', 'telefone_emergencia', 'unidade', 'usuario']
        labels = {
            'nome': 'Nome Funcionário','CPF':'CPF do Funcionário', 'endereco': 'Endereço Funcionário', 'telefone': 'Telefone',
            'telefone_emergencia': 'Telefone de Emergência', 'usuario': 'Usuário a ser vinculado','unidade': 'Unidade do Fucionário'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome do Funcionário'}),
            'CPF': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF Funcionário Exemplo: 123.456.789-11'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Endereço do Funcionário'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Telefone Exemplo: (21)91234-5678'}),
            'telefone_emergencia': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone Para Casos de Emergência'}),
            'unidade': forms.Select(attrs={'class': 'form-select', 'selected': 'Selecione a Unidade'}),
            'usuario': forms.Select(attrs={'class': 'form-select', 'selected': 'Vincule a um usuário'})
        }