from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    numero_telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username


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
