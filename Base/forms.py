from django.contrib.auth.models import User
from django import forms 
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        label =  {'username': 'Usuário', 'password': 'Senha'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu Usuário'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua Senha'}),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].help_text = ''
            self.fields['password'].help_text = ''

