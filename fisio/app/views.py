from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Agendamento
from django.contrib import messages

def index(request):
    context = {}
    return render(request, 'index.html', context)

def sobrenos(request):
    context = {}
    return render(request, 'sobrenos.html', context)

def faleconosco(request):
    context = {}
    return render(request, 'faleconosco.html', context)

def agendamento(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_consulta = request.POST.get('data')
        horario_consulta = request.POST.get('horario')
        mensagem_adicional = request.POST.get('mensagem')

        # Crie uma instância do modelo Agendamento e salve no banco de dados
        agendamento = Agendamento(
            nome=nome,
            email=email,
            telefone=telefone,
            data_consulta=data_consulta,
            horario_consulta=horario_consulta,
            mensagem_adicional=mensagem_adicional
        )
        agendamento.save()

        # Adicione a mensagem de confirmação
        messages.success(request, 'Consulta agendada com sucesso!')

        # Redirecione para a mesma página ou a página inicial
        return redirect('index')  # Substitua 'nome_da_sua_url' pela URL desejada
    else:
        # Renderize o formulário de agendamento
        return render(request, 'agendamento.html')



def erro(request):
    context = {}
    return render(request, '404.html', context)

def detail(request, question_id):
    context = {}
    return render(request, 'detail.html', context)

def results(request, question_id):
    response = "Essa é a página de resultados da questão %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Essa é a página de votação da questão %s." % question_id)