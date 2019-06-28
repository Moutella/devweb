from django.db.models import Sum, F, FloatField
from django.shortcuts import render, get_object_or_404, redirect

from produto.forms import ProdutoForm, RemoveProdutoForm
from produto.models import Produto

def cadastra_produto(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.user=request.user
            produto.save()

            lista_de_produtos = []
            lista_de_produtos.append(produto)

            resultado = Produto.objects.filter(disponivel=True).aggregate(
                valor_do_estoque=Sum(F('estoque') * F('preco'), output_field=FloatField()))

            if resultado['valor_do_estoque']:
                valor_do_estoque = '{0:.2f}'.format(resultado['valor_do_estoque'])
            else:
                valor_do_estoque = '0,00'

            return render(request, 'produto/lista_de_produtos.html',
                          {'produtos': lista_de_produtos,
                           'valor_do_estoque': valor_do_estoque})

    else:
        form = ProdutoForm()

    produtos = Produto.objects.all()

    valor_do_estoque = 0
    ids_dos_produtos = []
    for produto in produtos:
        valor_do_estoque = valor_do_estoque + produto.preco * produto.estoque
        ids_dos_produtos.append(produto.id)

    return render(request, 'produto/cadastra_produto.html', {'form': form,
                                                             'produtos': produtos,
                                                             'valor_do_estoque': valor_do_estoque,
                                                             'ids_dos_produtos': ids_dos_produtos})


def remove_produto(request):
    print('Entrou em remove_produto')
    form = RemoveProdutoForm(request.POST)
    if form.is_valid():
        produto = get_object_or_404(Produto, pk=form.cleaned_data['produto_id'])
        print(produto)
        if request.user == produto.user:
            produto.delete()

            resultado = Produto.objects.filter(disponivel=True).aggregate(
                valor_do_estoque=Sum(F('estoque') * F('preco'), output_field=FloatField()))

            if resultado['valor_do_estoque']:
                valor_do_estoque = '{0:.2f}'.format(resultado['valor_do_estoque'])
            else:
                valor_do_estoque = '0,00'

            return render(request, 'produto/valor_do_estoque.html',
                          {'valor_do_estoque': valor_do_estoque})
        else:
            raise ValueError(request.user.first_name + ' tentando remover produto de outro usuário.')
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar remover um produto!')
