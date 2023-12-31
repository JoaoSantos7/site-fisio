from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_consulta = models.DateField()
    horario_consulta = models.TimeField()
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
