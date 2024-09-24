import django_filters
from .models import *
from .forms import *
from Adm.models import Unidades


class FilterFaltas(django_filters.FilterSet):
    nome = django_filters.ModelChoiceFilter( label= 'Filtrar por Nome', field_name="falta__nome",queryset= Faltas.objects.all(),
    widget= forms.Select(attrs={'class': 'form-select'}))
    unidade = django_filters.ModelChoiceFilter( label= 'Filtrar por Unidade', field_name="falta__unidade",queryset= Unidades.objects.all(),
    widget= forms.Select(attrs={'class': 'form-select'}))
    data_inicio_gte = django_filters.DateFilter(field_name='data', lookup_expr='gte', label= 'Data Início',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    data_fim_lte = django_filters.DateFilter(field_name='data', lookup_expr='lte', label= 'Data Fim',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    class Meta:
        model = Faltas
        fields = ['nome','unidade','data']
        
class FiltersPontoEntrada(django_filters.FilterSet):
    unidade = django_filters.ModelChoiceFilter(label = 'Filtrar por Unidade',field_name = 'usuario__unidade', queryset=Unidades.objects.all(),
        widget= forms.Select(attrs={'class': 'form-select'}))
    data_inicio = django_filters.DateFilter(field_name='data', lookup_expr='gte', label='Data Início',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    data_fim = django_filters.DateFilter(field_name='data', lookup_expr='lte', label= 'Data Fim',
        widget= forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    class Meta:
        model = PontoEntrada
        fields = ['unidade', 'data',]

class FiltersPontoSaida(django_filters.FilterSet):
    unidade = django_filters.ModelChoiceFilter(label = 'Filtrar por Unidade',field_name = 'usuario__unidade', queryset=Unidades.objects.all(),
        widget= forms.Select(attrs={'class': 'form-select'}))
    data_inicio = django_filters.DateFilter(field_name='data', lookup_expr='gte', label='Data Início',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    data_fim = django_filters.DateFilter(field_name='data', lookup_expr='lte', label= 'Data Fim',
        widget= forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    class Meta:
        model = PontoSaida
        fields = ['unidade', 'data',]

class PontoEntradaFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='data', lookup_expr='gte', label='Data Início',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    data_fim = django_filters.DateFilter(field_name='data', lookup_expr='lte', label= 'Data Fim',
        widget= forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    class Meta:
        model = PontoEntrada
        fields = ['data',]
        
class PontoSaidaFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='data', lookup_expr='gte', label='Data Início',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    data_fim = django_filters.DateFilter(field_name='data', lookup_expr='lte', label= 'Data Fim',
        widget= forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    class Meta:
        model = PontoSaida
        fields = ['data',]
        
class AtrasosFilter(django_filters.FilterSet):
    nome = django_filters.ModelChoiceFilter( label= 'Filtrar por Nome', field_name="funcionarios__nome",queryset= Faltas.objects.all(),
    widget= forms.Select(attrs={'class': 'form-select'}))
    unidade = django_filters.ModelChoiceFilter( label= 'Filtrar por Unidade', field_name="funcionarios__unidade",queryset= Unidades.objects.all(),
    widget= forms.Select(attrs={'class': 'form-select'}))
    data_inicio_gte = django_filters.DateFilter(field_name='data', lookup_expr='gte', label= 'Data Início',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    data_fim_lte = django_filters.DateFilter(field_name='data', lookup_expr='lte', label= 'Data Fim',
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    class Meta:
        model = Atrasos
        fields = ['nome','unidade','data']