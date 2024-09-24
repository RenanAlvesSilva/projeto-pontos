from django.db import models
from Adm.models import *
from django.contrib.auth.models import User

class Faltas(models.Model):
    falta = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, blank=False, null=True)
    
    class Meta:
        db_table = 'Faltas'
        verbose_name = 'Falta'
        verbose_name_plural = 'Faltas'
        
    def __str__(self):
        return self.falta.nome
    

class PontoEntrada(models.Model):
    usuario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    endereco = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.usuario}"
    
class PontoSaida(models.Model):
    usuario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    endereco = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.usuario}"
    

class Atrasos(models.Model):
    funcionarios = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    atraso = models.IntegerField(blank= False, null=True)
    data = models.DateField(auto_now_add=True, blank=False, null=True)
    
    class Meta:
        db_table = 'Atrasos'
        verbose_name = 'Atraso'
        verbose_name_plural = 'Atraso'
    
    def converter_atrasos(self):
        horas = self.atraso // 60
        minutos = self.atraso % 60
        return f'{horas} Horas - {minutos} Minutos'     
    
    def __str__(self):
        return self.funcionario.nome