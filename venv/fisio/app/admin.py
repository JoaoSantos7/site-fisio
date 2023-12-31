from django.contrib import admin
from .models import Question, Choice, Agendamento

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_consulta', 'horario_consulta',  'tipo_consulta', 'convenio', 'data_agendamento')
    search_fields = ('nome', 'email', 'data_consulta', 'horario_consulta'  'tipo_consulta', 'convenio')
    list_filter = ('data_consulta', 'horario_consulta',  'tipo_consulta', 'convenio', 'data_agendamento') 

admin.site.register(Agendamento, AgendamentoAdmin)

admin.site.register(Question)
admin.site.register(Choice)

