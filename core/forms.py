from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Orcamento


class CadastroUsuarioForm(forms.Form):

    # Dados do usuário
    username = forms.CharField(label="Nome de Usuário", max_length=150)
    first_name = forms.CharField(label="Nome", max_length=30)
    last_name = forms.CharField(label="Sobrenome", max_length=150)
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    # Dados do perfil
    telefone = forms.CharField(label="Telefone", max_length=20)
    idade = forms.IntegerField(label="Idade")
    genero = forms.ChoiceField(choices=Perfil.GENERO_CHOICES)
    foto = forms.ImageField(required=False)


class OrcamentoForm(forms.ModelForm):

    class Meta:
        model = Orcamento
        fields = ['titulo', 'descricao']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do orçamento'
            }),

            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descreva o que você precisa...'
            })
        }