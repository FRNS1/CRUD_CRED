from datetime import datetime as date

from django.db import models
from django.utils import timezone

# Create your models here.


class solicitacao(models.Model):

    nome_cliente = models.CharField(
        max_length=50, db_column='nome_cliente', blank=True, default=None, null=True)
    cnpj = models.CharField(max_length=14, db_column='cnpj',
                            blank=True, default=None, null=True, unique=True)
    valor_emprestimo = models.DecimalField(
        max_digits=10, decimal_places=2, db_column='valor_emprestimo', blank=True, default=None, null=True)
    faturamento_ano = models.DecimalField(
        max_digits=10, decimal_places=2, db_column='faturamento_ano', blank=True, default=None, null=True)
    nome_solicitante = models.CharField(
        max_length=50, db_column='nome_solicitante', blank=True, default=None, null=True)
    cpf_solicitante = models.CharField(
        max_length=11, db_column='cpf_solicitante', blank=True, default=None, null=True)
    telefone_solicitante = models.CharField(
        max_length=11, db_column='telefone_solicitante', blank=True, default=None, null=True)
    email_solicitante = models.CharField(
        max_length=70, db_column='email_solicitante', blank=True, default=None, null=True)
    data_solicitacao = models.DateTimeField(
        db_column='data_solicitacao', blank=True, default=timezone.now(), null=True)
    endereco_empresa = models.CharField(
        max_length=200, db_column='endereco_empresa', blank=True, default=None, null=True)

    class Meta:
        managed = True
        db_table = 'solitacao'
        verbose_name = 'solicitacao'
        verbose_name_plural = 'solicitacao'

    def __str__(self):
        return str(self.nome_cliente)
