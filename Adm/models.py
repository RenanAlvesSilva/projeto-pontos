from django.db import models
from django.contrib.auth.models import User

class Unidades(models.Model):
    name_unidade = models.CharField(max_length=20, blank=False, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    class Meta:
        db_table = 'Unidades'
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        
    def __str__(self):
        return self.name_unidade
    
class Funcionarios(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=True)
    usuario = models.OneToOneField(User, related_name='funcionario', on_delete=models.CASCADE, null=True)
    CPF = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100, blank=False, null=True)
    telefone = models.CharField(max_length=14, blank=False, null=True)
    telefone_emergencia = models.CharField(max_length=14, blank=True, null= True)
    unidade = models.ForeignKey(Unidades,related_name='unidades', on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    
    
    class Meta:
        db_table= 'Funcionários'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    
    def __str__(self):
        return self.nome
    
