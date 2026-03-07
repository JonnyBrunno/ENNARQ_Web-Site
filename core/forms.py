from django import forms
from .models import Orcamento

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do Orçamento'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva o que você precisa...'}),
        }
