from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from .filters import *
from .forms import *
from .models import *

# Create your views here.


def login_page(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('solicitacoes/')
        else:
            return redirect('/')

    else:
        return render(request, 'pages/login.html')


def solicitacoes(request):

    solicitacoes_filter = FilterSolicitacoes(
        request.GET, queryset=solicitacao.objects.all())

    paginated_solicitacoes = Paginator(solicitacoes_filter.qs, 10)
    page_number = request.GET.get('page')
    solicitacoes_obj = paginated_solicitacoes.get_page(page_number)

    context = {'solicitacoes_filter': solicitacoes_filter,
               'solicitacoes_obj': solicitacoes_obj}

    return render(request, 'pages/homepage.html', context)


def cadastrar_solicitacao(request):

    form = CadastroSolicitacao(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            email_solicitante = request.POST.get('email_solicitante')
            print(email_solicitante)

            cpf_solicitante = request.POST.get('cpf_solicitante')
            print(len(cpf_solicitante))

            cnpj = request.POST.get('cnpj')
            print(len(cnpj))

            if len(cnpj) != 14:
                print(
                    'Não passou o CNPJ ------------------------------------------------------')
                messages.info(
                    request, 'CNPJ inválido, verifique se ele possui 14 dígitos.')
            else:
                if len(cpf_solicitante) != 11:
                    messages.info(
                        request, 'CPF inválido, verifique se ele possui 14 dígitos.')
                else:
                    if '@' not in email_solicitante:
                        messages.info(
                            request, 'E-mail inválido.')
                    else:
                        form.save()
                        return redirect('solicitacoes/')

    data = date.today()

    context = {'form': form}

    return render(request, 'pages/cadastro.html', context)


def delete_solicitacao(request, id):

    solicitacao_linha = solicitacao.objects.get(id=id)
    solicitacao_linha.delete()
    return redirect('solicitacoes_emprestimo:solicitacoes')


class UpdateSolicitacao(UpdateView):
    model = solicitacao
    template_name = 'pages/atualiza.html'
    fields = ['nome_cliente', 'cnpj', 'valor_emprestimo', 'faturamento_ano',
              'nome_solicitante', 'cpf_solicitante', 'telefone_solicitante', 'email_solicitante']
    success_url = reverse_lazy('solicitacoes_emprestimo:solicitacoes')
