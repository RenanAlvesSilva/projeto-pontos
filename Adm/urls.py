from django.urls import path
from .views import *

urlpatterns = [
   path('funcionarios', Funcionario, name='Funcionarios'),
   path('cadastrar', CadastrarFuncionario, name='cadastrarFuncionarios'),
   path('deletar/<str:id>', DeletarFuncionario, name='DeletarFuncionario'),
]
