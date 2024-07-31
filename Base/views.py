from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    return render(request,'dashboard/base.html')

def Logout_User(request):
    logout(request)
    return redirect(Login)