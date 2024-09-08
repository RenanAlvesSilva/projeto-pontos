from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Adm.models import Funcionarios
from django.db.models import Count
from Controle.models import Faltas


def Login(request):
    if request.method == 'GET':
      UserForms = UserForm()
      context = {'UserForms': UserForms}
      return render(request,'login/login.html', context)
    
    if request.method == 'POST':
        UserForms = UserForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password= password)
        
        if user is not None:
          login(request,user)
          return redirect(Dashboard)
        else:
          error = 'Usuário ou Senha inválida, verifique e tente novamente.'
          messages.warning(request, error)
          UserForms = UserForm()
          context = {'UserForms': UserForms}
          return render(request,'login/login.html', context)
    return render(request, 'login/login.html', context)
  
@login_required(login_url='Login')       
def Dashboard(request):
    model = Funcionarios.objects.all().aggregate(cont_funcionario = Count('id'))['cont_funcionario']
    faltas = Faltas.objects.all().aggregate(cont_faltas = Count('id'))['cont_faltas']
    context = {'model': model,
               'faltas': faltas,
               'is_operador': request.user.groups.filter(name='Operador').exists(),
               'is_gerencia': request.user.groups.filter(name='Gerencia').exists(),
               }
    return render(request,'dashboard/base.html', context)

def Logout_User(request):
    logout(request)
    return redirect(Login)