from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from produto.models import Produto, Categoria
from nostalgiastore import settings
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ("usuario_id", 'nome', 'email', 'nascimento', 'cpf', 'data_cadastro')

    usuario_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    nome = forms.CharField(
        error_messages={'required': 'Campo Obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
        required=True)
    email = forms.CharField(
        error_messages={'required': 'Campo Obrigatório',
                        'unique': 'E-mail já cadastrado.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
        required=True)
    cpf = forms.CharField(
        error_messages={'required': 'Campo Obrigatório',
                        'unique': 'CPF Já cadastrado.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '11'}),
        required=True)
    nascimento = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)
    data_cadastro = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

class RemoveUsuarioForm(forms.Form):
    class Meta:
        fields = ('usuario_id')

    usuario_id = forms.CharField(widget=forms.HiddenInput(), required=True)

class PesquisaUsuarioForm(forms.Form):
    class Meta:
        fields = ('buscaPor')

    buscaPor = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=False)