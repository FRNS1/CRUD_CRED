import django_filters

from .models import *


class FilterSolicitacoes(django_filters.FilterSet):

    class Meta:
        model = solicitacao
        fields = {
            'nome_cliente': ['icontains'],
            'cnpj': ['icontains'],
            'valor_emprestimo': ['icontains'],
            'faturamento_ano': ['icontains'],
            'data_solicitacao': ['icontains'],
        }
