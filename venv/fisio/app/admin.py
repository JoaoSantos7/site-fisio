from django.contrib import admin
from .models import Question, Choice, Agendamento

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_consulta', 'horario_consulta')
    search_fields = ('nome', 'email', 'data_consulta', 'horario_consulta')
    list_filter = ('data_consulta', 'horario_consulta')

admin.site.register(Agendamento, AgendamentoAdmin)

admin.site.register(Question)
admin.site.register(Choice)

