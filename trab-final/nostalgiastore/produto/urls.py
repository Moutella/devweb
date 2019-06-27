from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('<int:id>/<slug:slug_do_produto>/', views.pagina_produto, name='pagina_produto'),
    path('categoria/<slug:slug_da_categoria>/', views.categoria, name='lista_categoria'),
    path('cadastra_usuario/', views.cadastra_usuario, name='cadastra_usuario'),
    path('exibe_usuario/<int:id>/', views.exibe_usuario, name='exibe_usuario'),
    path('edita_usuario/<int:id>/', views.edita_usuario, name='edita_usuario'),
    path('remove_usuario/', views.remove_usuario, name="remove_usuario"),
    path('pesquisa_usuario/', views.pesquisa_usuario, name='pesquisa_usuario'),    
    path('exibe_usuarios/', views.exibe_usuarios, name='exibe_usuarios'),
]
