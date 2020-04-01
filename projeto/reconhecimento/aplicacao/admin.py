from django.contrib import admin
from .models import Departamento
from .models import Funcionario

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Funcionario)
