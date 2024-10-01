from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.utils import timezone
import datetime
from decouple import config



@login_required(login_url='Login')
def ControleFaltas(request):
    model = Faltas.objects.select_related('falta__unidade').all()
    FiltersFalta = FilterFaltas(request.GET, queryset= model)
    if FiltersFalta.is_valid():
        queryset = FiltersFalta.qs
    else:
        queryset = model
    FaltasPagination = Paginator(queryset, 6)
    page = request.GET.get('page')
    PaginarFaltas = FaltasPagination.get_page(page)
    context = {'PaginarFaltas': PaginarFaltas, 'FiltersFalta': FiltersFalta }
    return render(request, 'faltas/faltas.html', context= context)

@login_required(login_url='Login')
def CadastroFaltas(request):
    if request.method == 'GET':
        Falta = FaltasForms()
        context = {
            'FaltaForms': Falta
        }
        return render(request, 'faltas/cadastrofaltas.html', context)
    if request.method == 'POST':
        Falta = FaltasForms(request.POST)
        context = {
            'FaltaForms': Falta
        }
        if Falta.is_valid():
            Falta.save()
            sucesso = f'Você cadastrou uma falta para o funcionário'
            messages.success(request,sucesso)
            return redirect(ControleFaltas)
    return render(request, 'faltas/faltas.html')

def DeletarFaltas(request, id):
    model = get_object_or_404(Faltas, id=id)
    model.delete()
    aviso = f'Você deletou a falta do Funcionário'
    messages.warning(request, aviso)
    return redirect(ControleFaltas)

# Chave da minha API Google
GOOGLE_MAPS_API_KEY = config('GOOGLE_MAPS_API_KEY')

@csrf_exempt
def receive_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if latitude is None or longitude is None:
                return JsonResponse({'status': 'error', 'message': 'Latitude ou longitude ausente'}, status=400)

            # Usando a API do google maps para geocodificação
            geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&language=pt-BR&key={GOOGLE_MAPS_API_KEY}'
            response = requests.get(geocode_url)
            result = response.json()
            funcionario = get_object_or_404(Funcionarios, usuario=request.user)
            if result.get('status') == 'OK':
                # Obtenha o endereço formatado
                address = result['results'][0]['formatted_address']
                model = PontoEntrada.objects.create(endereco=address, data=datetime.datetime.now(), horario=timezone.localtime(), usuario=funcionario)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Nenhum endereço encontrado'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método de requisição inválido'}, status=405)

def ponto_view(request):
    address = request.GET.get('address', None)
    erro = request.GET.get('error', None)
    status = request.GET.get('status', None)
    registros = Funcionarios.objects.select_related('funcionario').all()
    context = {
        'address': address, 'error': erro, 'status': status, 'registros': registros,
    }
    return render(request, 'area-funcionarios/registrar_ponto.html', context)


login_required(login_url='Login')
def ListarPontos(request):
    model = PontoEntrada.objects.select_related('usuario__usuario')
    FiltersPontos= FiltersPontoEntrada(request.GET, queryset= model)
    if FiltersPontos.is_valid():
        queryset = FiltersPontos.qs
    else:
        queryset = model
    PontosPagination = Paginator(queryset, 6)
    page = request.GET.get('page')
    PaginarPontos = PontosPagination.get_page(page)
    context = {'PaginarPontos': PaginarPontos, 'FiltersPontos': FiltersPontos }
    return render(request, 'pontos/listarPontos.html', context= context)

def Deletar_ponto(request, id):
    model = PontoEntrada.objects.get(id=id)
    model.delete()
    aviso = 'Ponto deletado com sucesso.'
    messages.success(request, aviso)
    return redirect('ListarPontos')


@csrf_exempt
def receive_location_saida(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if latitude is None or longitude is None:
                return JsonResponse({'status': 'error', 'message': 'Latitude ou longitude ausente'}, status=400)

            # Usando a API do google maps para geocodificação
            geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&language=pt-BR&key={GOOGLE_MAPS_API_KEY}'
            response = requests.get(geocode_url)
            result = response.json()
            funcionario = get_object_or_404(Funcionarios, usuario=request.user)
            if result.get('status') == 'OK':
                # Obtenha o endereço formatado
                address = result['results'][0]['formatted_address']
                model = PontoSaida.objects.create(endereco=address, data=datetime.datetime.now(), horario=timezone.localtime(), usuario=funcionario)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Nenhum endereço encontrado'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método de requisição inválido'}, status=405)

def ponto_view_saida(request):
    address = request.GET.get('address', None)
    erro = request.GET.get('error', None)
    status = request.GET.get('status', None)
    context = {
        'address': address, 'error': erro, 'status': status,
    }
    return render(request, 'area-funcionarios/registrar_ponto_saida.html', context)

def listar_meuspontos_entrada(request):
    funcionario = get_object_or_404(Funcionarios, usuario=request.user)

    ponto_entrada_filter = PontoEntradaFilter(request.GET, queryset=PontoEntrada.objects.filter(usuario=funcionario))
    ponto_saida_filter = PontoSaidaFilter(request.GET, queryset=PontoSaida.objects.filter(usuario=funcionario))

    pontos = []
    for ponto in ponto_entrada_filter.qs:
        pontos.append({'ponto': ponto, 'tipo': 'Entrada'})
    for ponto in ponto_saida_filter.qs:
        pontos.append({'ponto': ponto, 'tipo': 'Saída'})

    context = {
        'pontos': pontos,
        'ponto_entrada_filter': ponto_entrada_filter,
        'ponto_saida_filter': ponto_saida_filter,
    }
    return render(request, 'area-funcionarios/listar_meuspontos_entrada.html', context)

login_required(login_url='Login')
def ListarSaida(request):
    model = PontoSaida.objects.select_related('usuario__usuario')
    FiltersPontos= FiltersPontoSaida(request.GET, queryset= model)
    if FiltersPontos.is_valid():
        queryset = FiltersPontos.qs
    else:
        queryset = model
    PontosPagination = Paginator(queryset, 6)
    page = request.GET.get('page')
    PaginarPontos = PontosPagination.get_page(page)
    context = {'PaginarPontos': PaginarPontos, 'FiltersPontos': FiltersPontos }
    return render(request, 'pontos/listarPontosSaida.html', context= context)

def Deletar_pontoSaida(request, id):
    model = PontoSaida.objects.get(id=id)
    model.delete()
    aviso = 'Ponto deletado com sucesso.'
    messages.success(request, aviso)
    return redirect('ListarSaida')

@login_required(login_url='Login')
def CadastroAtrasos(request):
    if request.method == 'GET':
        atrasos = AtrasosForms()
        context = {
            'AtrasosForms': atrasos
        }
        return render(request, 'atrasos/cadastroatraso.html', context)
    if request.method == 'POST':
        atraso = AtrasosForms(request.POST)
        context = {
            'AtrasosForms': atraso
        }
        if atraso.is_valid():
            atraso.save()
            sucesso = f'Você cadastrou um atraso para o funcionário'
            messages.success(request,sucesso)
            return redirect('ControleAtrasos')
    return render(request, 'atrasos/atrasos.html')

@login_required(login_url='Login')
def ControleAtrasos(request):
    model = Atrasos.objects.select_related('funcionarios__unidade').all()
    atrasoFilter = AtrasosFilter(request.GET, queryset= model)
    if atrasoFilter.is_valid():
        queryset = atrasoFilter.qs
    else:
        queryset = model
    AtrasosPaginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    AtrasosPaginator = AtrasosPaginator.get_page(page)
    context = {'AtrasosPaginator': AtrasosPaginator, 'AtrasosFilter': atrasoFilter }
    return render(request, 'atrasos/atrasos.html', context= context)

def Deletar_Atrsos(request, id):
    model = Atrasos.objects.get(id=id)
    model.delete()
    aviso = 'Atraso deletado com sucesso.'
    messages.success(request, aviso)
    return redirect('ControleAtrasos')
