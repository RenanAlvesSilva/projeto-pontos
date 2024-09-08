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



@login_required(login_url='Login')
def ControleFaltas(request):
    model = Faltas.objects.all()
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
        return render(request, 'faltas/cadastroFaltas.html', context)
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
GOOGLE_MAPS_API_KEY = 'AIzaSyCpgtfvqlPmspg9L7zPzme3cXwIvTdDFdo'

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

            if result.get('status') == 'OK':
                # Obtenha o endereço formatado
                address = result['results'][0]['formatted_address']
                model = PontoEntrada.objects.create(endereco=address, data=datetime.datetime.now(), horario=timezone.localtime(), usuario=request.user)
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
    model = PontoEntrada.objects.all()
    FiltersPontos= FilterFaltas(request.GET, queryset= model)
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

            if result.get('status') == 'OK':
                # Obtenha o endereço formatado
                address = result['results'][0]['formatted_address']
                model = PontoSaida.objects.create(endereco=address, data=datetime.datetime.now(), horario=timezone.localtime(), usuario=request.user)
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
    entrada = PontoEntrada.objects.filter(usuario=request.user)
    context = {'entrada': entrada}
    return render(request, 'area-funcionarios/listar_meuspontos_entrada.html', context)