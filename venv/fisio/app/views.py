from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Agendamento
from django.contrib import messages
from datetime import datetime, time
from django import forms

def index(request):
    context = {}
    return render(request, 'index.html', context)

def sobrenos(request):
    context = {}
    return render(request, 'sobrenos.html', context)

def faleconosco(request):
    context = {}
    return render(request, 'faleconosco.html', context)

# Agendamento

def agendamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_consulta = request.POST.get('data')
        horario_consulta = request.POST.get('horario')
        mensagem_adicional = request.POST.get('mensagem')
        tipo_consulta = request.POST.get('tipo_consulta')
        convenio = request.POST.get('convenio')

        if tipo_consulta == 'particular':
            convenio = None
        else:
            convenio = request.POST.get('convenio')

        # Chame a função de validação
        if validar_horario_consulta(data_consulta, horario_consulta):
            # Crie uma instância do modelo Agendamento e salve no banco de dados
            agendamento = Agendamento(
                nome=nome,
                email=email,
                telefone=telefone,
                data_consulta=data_consulta,
                horario_consulta=horario_consulta,
                tipo_consulta=tipo_consulta,
                convenio=convenio,
                mensagem_adicional=mensagem_adicional
            )
            agendamento.save()

            # Adicione a mensagem de confirmação
            messages.success(request, 'Consulta agendada com sucesso!')

            # Redirecione para a mesma página ou a página inicial
            return redirect('index')  # Substitua 'nome_da_sua_url' pela URL desejada
        else:
            # Adicione a mensagem de erro
            messages.error(request, 'Não podemos agendar sua consulta para este horário ou dia. Verifique nosso horário de funcionamento abaixo no nosso rodapé.')

    # Renderize o formulário de agendamento
    context = {}
    return render(request, 'agendamento.html', context)

def validar_horario_consulta(data_consulta, horario_consulta):
    # Converta a data fornecida para um objeto datetime
    data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()

    # Converta o horário fornecido para um objeto time
    horario_consulta = datetime.strptime(horario_consulta, '%H:%M').time()

    # Combine a data e horário fornecidos para um objeto datetime
    data_hora_consulta = datetime.combine(data_consulta, horario_consulta)

    # Defina os horários de funcionamento da clínica
    horario_abertura = time(9, 0)  # 09:00 am
    horario_fechamento_semana = time(22, 0)  # 10:00 pm
    horario_fechamento_sabado = time(20, 0)  # 08:00 pm

    # Verifique se o horário da consulta está dentro do horário de funcionamento
    if (
        (data_hora_consulta.weekday() < 5 and horario_abertura <= data_hora_consulta.time() <= horario_fechamento_semana) or
        (data_hora_consulta.weekday() == 5 and horario_abertura <= data_hora_consulta.time() <= horario_fechamento_sabado)
    ):
        return True
    else:
        return False
    
# Fim do Agendamento

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