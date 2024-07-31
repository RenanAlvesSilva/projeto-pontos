from django.urls import path
from .views import *

urlpatterns = [
   path('funcionarios', Funcionarios, name='Funcionarios'),
   path('cadastrar', CadastrarFuncionario, name='cadastrarFuncionarios')
]
