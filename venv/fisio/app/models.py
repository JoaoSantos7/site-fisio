from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=False)
    username = models.CharField(max_length=255, null=True, blank=False)
    email = models.CharField(max_length=255, null=True, blank=False)
    data_nascimento = models.DateField(null=True, blank=False)
    numero_telefone = models.CharField(max_length=15, null=True, blank=False)

    def __str__(self):
        return self.user.username


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_consulta = models.DateField()
    horario_consulta = models.TimeField()
    tipo_consulta = models.CharField(max_length=20, choices=[('particular', 'Particular'), ('convenio', 'Convênio')])
    convenio = models.CharField(max_length=20, blank=True, null=True, choices=[('unimed', 'Unimed'), ('iasep', 'Iasep'), ('hapvida', 'Hapvida'), ('seila', 'Sei La')])
    mensagem_adicional = models.TextField()
    data_agendamento = models.DateTimeField(auto_now_add=True)  # Adiciona a data/hora do agendamento

    def __str__(self):
        return f"{self.nome} - {self.data_consulta} - {self.horario_consulta}"
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
