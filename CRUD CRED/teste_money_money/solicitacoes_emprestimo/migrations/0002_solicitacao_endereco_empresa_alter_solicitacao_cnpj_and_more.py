# Generated by Django 4.0 on 2023-01-15 23:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes_emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='endereco_empresa',
            field=models.CharField(blank=True, db_column='endereco_empresa', default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='cnpj',
            field=models.CharField(blank=True, db_column='cnpj', default=None, max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='data_solicitacao',
            field=models.DateTimeField(blank=True, db_column='data_solicitacao', default=datetime.datetime(2023, 1, 15, 23, 7, 9, 515139, tzinfo=utc), null=True),
        ),
    ]