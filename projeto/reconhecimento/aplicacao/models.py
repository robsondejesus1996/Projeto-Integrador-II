import random
import os
from django.db import models
from django import forms


# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    #dt_criacao = models.DateTimeField(auto_now_add=True)#criação que pode ser de funcionario(data nascimento)
    def __str__(self):
         return self.nome

class Funcionario(models.Model):
     nome = models.CharField(max_length=100)
     data_nascimento = models.DateField(null=True, blank=True)
     endereco = models.CharField(max_length=200)
     telefone = models.CharField(max_length=200)
     #relacionamento 1 para n(um depratamento tem vários funcionarios) (1 ou muitos funcionarios pertencem a 1 dep)
     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
     estado_civil = models.CharField(max_length=200)
     email = models.CharField(max_length=200)
     cpf = models.CharField(max_length=200)
     salario = models.DecimalField(max_digits=8, decimal_places=4)
     models.ImageField(upload_to='images/')
     image = models.ImageField(upload_to='images/')
     

     class Meta:
         verbose_name_plural = 'Funcionarios'#difinir o nome em plural da entidade funcionario

    
     def __str__(self):
         return self.nome
