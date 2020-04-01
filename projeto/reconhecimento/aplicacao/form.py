from django.forms import ModelForm
from .models import Departamento
from .models import Funcionario



class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'localidade']


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'data_nascimento', 'endereco' , 'telefone', 'departamento', 'estado_civil' , 'email', 'cpf' , 'salario', 'image']

class Visualizador(ModelForm):
            class Meta:
                model = Funcionario
                fields = ['nome', 'data_nascimento', 'endereco', 'telefone', 'departamento', 'estado_civil', 'email',
                          'cpf', 'salario']





