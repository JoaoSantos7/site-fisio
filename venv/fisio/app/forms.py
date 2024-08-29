from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))
    data_nascimento = forms.DateField(label='Data de Nascimento', required=False)
    numero_telefone = forms.CharField(label='Número de Telefone', max_length=15, required=False)
    cpf = forms.CharField(label='CPF', max_length=11, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'cpf', 'email', 'data_nascimento', 'numero_telefone', 'password']
        labels = {
            'first_name': 'Nome',
            'username': 'Nome de Usuário',
            'email': 'Endereço de Email',
            'cpf': 'CPF',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
