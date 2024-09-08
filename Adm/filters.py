import django_filters
from .models import *
from .forms import *

class FilterFuncionarios(django_filters.FilterSet):
    unidade = django_filters.ModelChoiceFilter( label= 'Filter Unidade', queryset= Unidades.objects.all(),
     widget= forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Funcionarios
        fields = ['unidade',]
        
    