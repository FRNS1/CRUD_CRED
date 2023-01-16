from django import forms

from .models import *

# funções de validação


class CadastroSolicitacao(forms.ModelForm):
    class Meta:
        model = solicitacao
        fields = ['nome_cliente', 'cnpj', 'endereco_empresa', 'valor_emprestimo', 'faturamento_ano',
                  'nome_solicitante', 'cpf_solicitante', 'telefone_solicitante', 'email_solicitante']

# class CadastroSolicitacao(forms.ModelForm):
#     class Meta:
#         model = solicitacao
#         fields = '__all__'
