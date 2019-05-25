from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto


# Create your views here.
def index(request):
    produtos = Produto.objects.filter(disponivel=True).order_by("id")
    categorias = Categoria.objects.all().order_by("nome")

    print(produtos)
    return render(request, 'produto/index.html', {'produtos': produtos, 'categorias': categorias})



def pagina_produto(request, id, slug_do_produto):
    categorias = Categoria.objects.all().order_by("nome")
    produto = get_object_or_404(Produto, id=id, disponivel=True)
    return render(request, 'produto/produto.html', {'produto': produto, 'categorias': categorias})


def categoria(request, slug_da_categoria):
    categorias = Categoria.objects.all().order_by("nome")
    categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
    produtos = Produto.objects.filter(disponivel=True).order_by("nome")
    produtos = produtos.filter(categoria=categoria)

    return render(request, 'produto/categoria.html', {'categorias': categorias,
                                                  'produtos': produtos,
                                                  'categoria': categoria})