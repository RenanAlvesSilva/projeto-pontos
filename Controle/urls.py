from django.urls import path
from .views import *

urlpatterns = [
   path('faltas', ControleFaltas, name='Faltas'),
   path('cadastro_faltas', CadastroFaltas, name='CadastroFaltas'),
   path('deletar_falta/<int:id>', DeletarFaltas, name='DeletarFaltas'),
   path('send-location/', receive_location, name='api/send-location'),
   path('ponto', ponto_view, name='ponto_view'),
   path('listar-pontos', ListarPontos, name='ListarPontos'),
   path('deletar-ponto/<int:id>', Deletar_ponto, name='deletar_ponto'),
   path('send-location-out/', receive_location_saida, name='api/send-location-out'),
   path('registrar-ponto-saida', ponto_view_saida, name='ponto_saida'),
   path('listar-meus-pontos', listar_meuspontos_entrada, name='listar_meuspontos_entrada')
]
