from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))
    data_nascimento = forms.DateField(label='Data de Nascimento', required=False)
    numero_telefone = forms.CharField(label='Número de Telefone', max_length=15, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password', 'data_nascimento', 'numero_telefone']
        labels = {
            'first_name': 'Nome',
            'username': 'Nome de Usuário',
            'email': 'Endereço de Email',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
