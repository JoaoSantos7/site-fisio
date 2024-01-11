from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('erro/', views.erro, name='404'),
    path('sobrenos/', views.sobrenos, name='sobrenos'),
    path('faleconosco/', views.faleconosco, name='faleconosco'),
    path('agendamento/', views.agendamento, name='agendamento'),
    #path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)