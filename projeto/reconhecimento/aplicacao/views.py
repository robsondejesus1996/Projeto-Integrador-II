from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Funcionario
from .models import Departamento
from .form import DepartamentoForm
from .form import FuncionarioForm
from .form import Visualizador
import datetime


# Create your views here.

def login(request):
    return HttpResponse('Aqui sera a view de login futuramente!!!')

def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3']

    data ['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html', data)    

def listagem(request):
    data = {}
    data ['funcionarios'] = Funcionario.objects.all()
    return render(request, 'aplicacao/listagem.html', data)


def listagem_segurancao(request):
    buscar = request.GET.get('buscar')
    dados = {}
    dados ['funcionarios'] = Funcionario.objects.filter(cpf = buscar)
    return render(request, 'aplicacao/listagem_seguranca.html', dados)

def novo_departamento(request):
    data = {}
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'aplicacao/formDepartamento.html', data)

def novo_funcionario(request):
    data = {}
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'aplicacao/formFuncionario.html', data)







    
#update_dp, update_fun, delete_dp, delete_fun

def update_dp(request, pk):
    data = {}
    departamento = Departamento.objects.get(pk=pk)
    form = DepartamentoForm(request.POST or None, instance=departamento)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'aplicacao/formDepartamento.html', data)


def update_fun(request, pk):
    data = {}
    funcionario = Funcionario.objects.get(pk=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['funcionario'] = funcionario
    return render(request, 'aplicacao/formFuncionario.html', data)

#teste da visualização do seguranca para ver os funcionarios cadastrados
def visualizador_seg_fun(request, pk):
    data = {}
    funcionario = Funcionario.objects.get(pk=pk)
    form = Visualizador(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['funcionario'] = funcionario
    return render(request, 'aplicacao/visualizar_seg_fun.html', data)


def delete(request, pk):   
    funcionario = Funcionario.objects.get(pk=pk)
    funcionario.delete()     
    return redirect('url_listagem')

def reconhecer(request):
    return render(request, 'aplicacao/reconhecedor.html')




