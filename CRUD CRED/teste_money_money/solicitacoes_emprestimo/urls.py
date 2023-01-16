from django.contrib import admin
from django.urls import include, path

from .views import *

app_name = 'solicitacoes_emprestimo'

urlpatterns = [
    path('', login_page, name='login_page'),
    path('solicitacoes/', solicitacoes, name='solicitacoes'),
    path('cadastro', cadastrar_solicitacao, name='cadastrar_solicitacao'),
    path('atualiza/<int:pk>', UpdateSolicitacao.as_view(),
         name='UpdateSolicitacao'),
    path('delete/<int:id>', delete_solicitacao, name='delete_solicitacao'),
]
