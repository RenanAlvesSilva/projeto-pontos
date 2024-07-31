from django.shortcuts import render
from .forms import *
from django.contrib import messages


def Funcionarios(request):
    return render(request, 'Adm/funcionarios/funcionarios.html')


def CadastrarFuncionario(request):
    if request.method == 'GET':
      funcionariosForms = FuncionariosForm()
      context = {
          'funcionariosForms': funcionariosForms
      }
      return render(request, 'Adm/funcionarios/cadastro_funcionarios.html', context)

    if request.method =='POST':
        funcionariosForms = FuncionariosForm(request.POST)
        context = {'funcionariosForms': funcionariosForms}
        if funcionariosForms.is_valid():
            funcionariosForms.save()
            sucesso = f'Funcionário foi cadastrado com sucesso.'
            messages.success(request, sucesso)
            return render(request, 'Adm/funcionarios/funcionarios.html')
    return render(request, 'Adm/funcionarios/funcionarios.html', context)