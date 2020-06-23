from .models import Funcionario
from .form import DepartamentoForm
from .form import FuncionarioForm
from .form import Visualizador
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import cv2
from django.views.generic import CreateView
from .models import Departamento
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from flask import Flask, render_template, render_template_string, Response


class DeptoCreateView(CreateView):
    model = Departamento
    fields = ('nome', 'localidade')
    template_name = 'aplicacao/formDepartamento.html'

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ('nome', 'data_nascimento', 'endereco', 'telefone', 'departamento', 'estado_civil', 'email', 'cpf', 'salario','image')
    template_name = 'aplicacao/formFuncionario.html'

def index(request):
    if request.user.username == 'Rh':
        return render(request, 'aplicacao/indexreal.html')
    else:
        return render(request, 'aplicacao/indexseg.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)


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
    form = FuncionarioForm()
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    if request.method == 'POST':
        form = FuncionarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('url_listagem')
    data['form'] = form
    return render(request, 'aplicacao/formFuncionario.html', data)


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

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('url_listagem')

    data['form'] = form
    data['funcionario'] = funcionario

    return render(request, 'aplicacao/formFuncionario.html', data)

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

def voltar (request):
    return render (request, 'aplicacao/indexseg.html')

def voltarg(request):
    return  render(request, 'aplicacao/indexreal.html')

def detectar(request):
    classificador = cv2.CascadeClassifier("original.xml")
    camera = cv2.VideoCapture(0)

    while (True):
        conectado, imagem = camera.read()
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # testes a partir daqui
        facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100, 100))
        for (x, y, l, a) in facesDetectadas:
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        cv2.imshow('frame', imagem)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

    return HttpResponse('A face foi reconhecida com sucesso!!!')


def capturar(request):
    classificador = cv2.CascadeClassifier("original.xml")
    camera = cv2.VideoCapture(0)
    amostra = 1
    numeroAmostrars = 25
    id = input('Digite o identificador da pessoa: ')
    # nome = input('Digite o nome da pessoa: ')
    largura, altura = 220, 220
    print("Capturando as faces...")

    while (True):
        conectado, imagem = camera.read()
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))
        for (x, y, l, a) in facesDetectadas:
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
            cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            print("[Foto " + str(amostra) + " capturada com sucesso]")
            amostra += 1

        cv2.imshow('frame', imagem)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        elif (amostra >= numeroAmostrars + 1):
            break

    print("faces capturadas com sucesso")
    camera.release()
    cv2.destroyAllWindows()

    return HttpResponse('A face foi capturada com sucesso!!!')


def treinar(request):
    return HttpResponse('não esta funcionando está merda')


def reconhecer(request):

    detectorFace = cv2.CascadeClassifier("original.xml")
    reconhecedor = cv2.face.EigenFaceRecognizer_create()
    reconhecedor.read("classificadorEigen.yml")
    largura, altura = 220, 220
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    camera = cv2.VideoCapture(0)

    while (True):
        conectado, imagem = camera.read(    )
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))
        for (x, y, l, a) in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
            id, confianca = reconhecedor.predict(imagemFace)
            cv2.putText(imagem, str(id), (x, y + (a + 30)), font, 2, (0, 0, 255))
            # cv2.putText(imagem, str(confianca), (x, y + (a + 50)), font, 1, (0, 0, 255))

        cv2.imshow('frame', imagem)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

    return HttpResponse('A face foi reconhecida com sucesso!!!')


def funcionario_image_view(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FuncionarioForm()
    return render(request, 'formFuncionario.html', {'form': form})


def success(request):
    return HttpResponse('Cadastro concluído!')
