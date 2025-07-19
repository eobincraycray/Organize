from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', 'cor', 'prioridade_padrao', 'ativo']
        widgets = {
            'cor': forms.TextInput(attrs={'type': 'color'}),
        }