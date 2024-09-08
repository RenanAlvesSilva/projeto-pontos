from django.urls import path
from .views import *

urlpatterns = [
   path('funcionarios', Funcionario, name='Funcionarios'),
   path('cadastrar', CadastrarFuncionario, name='cadastrarFuncionarios'),
   path('deletar/<int:id>', DeletarFuncionario, name='DeletarFuncionario'),
   path('editar_funcionario/<int:id>', EditarFuncionarios, name='EditarFuncionarios'),
]
