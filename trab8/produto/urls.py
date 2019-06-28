from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('cadastra_produto/', views.cadastra_produto, name='cadastra_produto'),
    path('remove_produto/', views.remove_produto, name='remove_produto'),
]
