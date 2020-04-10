"""reconhecimento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from aplicacao.views import login, listagem, novo_departamento, novo_funcionario, update_dp, update_fun, delete, \
reconhecer, listagem_segurancao,visualizador_seg_fun, voltar, voltarg, capturar, treinar, reconhecer, detectar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listagem/', listagem, name ='url_listagem'),
    path('novadp/', novo_departamento, name = 'url_nova_dep'),
    path('novafun/', novo_funcionario, name = 'url_nova_fun'),
    path('listagemseg', listagem_segurancao, name = 'url_lisragem_seguranca'),
    path('reconhecer/', reconhecer, name = 'url_reconhecer_fun'),
    path('updatedp/<int:pk>/', update_dp, name = 'url_update_dp'),
    path('updatefun/<int:pk>/', update_fun, name = 'url_update_fun'),
    path('visualizar_seg_fun/<int:pk>/', visualizador_seg_fun, name = 'url_visualizar'),
    path('delete/<int:pk>/', delete, name = 'url_delete'),
    path('', include('aplicacao.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('voltar/', voltar, name = 'url_voltar'),
    path('voltarg/', voltarg, name = 'url_voltarg'),
    path('detectar/',detectar, name = 'url_detectar'),
    path('capturar/', capturar, name = 'url_capturar'),
    path('treinar/', treinar, name = 'url_treinar'),
    path('reconhecer/', reconhecer, name = 'url_reconhecer'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

