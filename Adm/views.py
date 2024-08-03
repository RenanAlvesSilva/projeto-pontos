from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='Login')
def Funcionario(request):
    model = Funcionarios.objects.all()
    context = {'model': model}
    return render(request, 'Adm/funcionarios/funcionarios.html', context)

@login_required(login_url='Login')
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
            return redirect(Funcionario)
    return render(request, 'Adm/funcionarios/funcionarios.html', context)


@login_required(login_url='Login')
def DeletarFuncionario(request, id):
    model = Funcionarios.objects.get(id=id)
    model.delete()
    return redirect(Funcionario)