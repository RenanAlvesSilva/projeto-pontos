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
        
class FiltersPotnos(django_filters.FilterSet):
    ...
        