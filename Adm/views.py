from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import *



@login_required(login_url='Login')
def Funcionario(request):
    model = Funcionarios.objects.all().order_by('nome')
    FiltersFuncionarios = FilterFuncionarios(request.GET, queryset= model)
    if FiltersFuncionarios.is_valid():
        queryset = FiltersFuncionarios.qs
    else:
        queryset = model
    FuncionariosPagination = Paginator(queryset, 6)
    page = request.GET.get('page')
    PaginarFuncionarios = FuncionariosPagination.get_page(page)
    context = {'PaginarFuncionarios': PaginarFuncionarios, 'FiltersFuncionarios': FiltersFuncionarios }
    return render(request, 'Adm/funcionarios/funcionarios.html', context= context)

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
            funcionario= request.POST.get('nome')
            sucesso = f'Funcionário {funcionario} foi cadastrado com sucesso.'
            messages.success(request, sucesso)
            return redirect(Funcionario)
    return render(request, 'Adm/funcionarios/funcionarios.html', context)


@login_required(login_url='Login')
def DeletarFuncionario(request, id):
    model = Funcionarios.objects.get(id=id)
    model.delete()
    aviso = f'O funcionário {model.nome} foi deletado com sucesso.'
    messages.warning(request, aviso)
    return redirect(Funcionario)

def EditarFuncionarios(request, id):
    model = get_object_or_404(Funcionarios, id=id)
    if request.method == 'GET':
        FuncionariosForms = FuncionariosForm(instance=model)
        context = {
            'FuncionariosForms': FuncionariosForms
        }
        return render(request, 'Adm/funcionarios/EditarFuncionarios.html', context)
    if request.method == 'POST':
        FuncionariosForms = FuncionariosForm(request.POST, instance=model)
        if FuncionariosForms.is_valid():
            FuncionariosForms.save()
            return redirect(Funcionario)
    return redirect('dashboard')
    
        