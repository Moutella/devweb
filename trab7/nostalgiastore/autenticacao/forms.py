from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import PasswordInput


class AuthenticationFormCustomizado(AuthenticationForm):

    username = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '20'}),
        required=True)

    # <input type="text"
    #        name="username"
    #        id="id_username"
    #        class="form-control form-control-sm"
    #        maxlength=""
    #        required>

    password = forms.CharField(
        min_length=5,
        error_messages={'required': 'Campo obrigatório.', },
        widget=PasswordInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)
