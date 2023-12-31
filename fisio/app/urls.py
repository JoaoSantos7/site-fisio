from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('erro/', views.erro, name='404'),
    path('sobrenos/', views.sobrenos, name='sobrenos'),
    path('faleconosco/', views.faleconosco, name='faleconosco'),
    path('agendamento/', views.agendamento, name='agendamento'),
    #path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
