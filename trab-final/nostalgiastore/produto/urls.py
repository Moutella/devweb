from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('<int:id>/<slug:slug_do_produto>/', views.pagina_produto, name='pagina_produto'),
    path('<slug:slug_da_categoria>/', views.categoria, name='lista_categoria'),
]
