from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from autenticacao.forms import AuthenticationFormCustomizado
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=AuthenticationFormCustomizado), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
