import random
import os
from django.db import models
from django import forms


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)#pegar o nome do arquivo aqui
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "accounts/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    #dt_criacao = models.DateTimeField(auto_now_add=True)#criação que pode ser de funcionario(data nascimento)
    def __str__(self):
         return self.nome

class Funcionario(models.Model):
     nome = models.CharField(max_length=100)
     data_nascimento = models.DateField(null=True, blank=True)
     endereco = models.CharField(max_length=100)
     telefone = models.CharField(max_length=100)
     #relacionamento 1 para n(um depratamento tem vários funcionarios) (1 ou muitos funcionarios pertencem a 1 dep)
     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
     estado_civil = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     cpf = models.CharField(max_length=100)
     salario = models.DecimalField(max_digits=8, decimal_places=4)
     image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
     

     class Meta:
         verbose_name_plural = 'Funcionarios'#difinir o nome em plural da entidade funcionario

    
     def __str__(self):
         return self.nome