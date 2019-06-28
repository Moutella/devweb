from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

#from .forms import
from .models import Categoria, Produto, Usuario
from .forms import UsuarioForm, RemoveUsuarioForm, PesquisaUsuarioForm


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

def cadastra_usuario(request):
    if request.POST:
        usuario_id = request.POST.get('usuario_id')
        if(usuario_id):
            usuario = get_object_or_404(Usuario, pk = usuario_id)
            usuario_form = UsuarioForm(request.POST, instance=usuario)
        else:
            usuario_form = UsuarioForm(request.POST)

        if(usuario_form.is_valid()):
            usuario = usuario_form.save(commit=False)
            if usuario_id:
                messages.add_message(request, messages.INFO, 'Usuario alterado com sucesso')
            else:
                messages.add_message(request, messages.INFO, 'Usuario criado!')
            usuario.save()
            return redirect('produto:exibe_usuario', id=usuario.id)
        else:
            messages.add_message(request, messages.ERROR, 'Resolva os erros')
    else:
        usuario_form = UsuarioForm()
    
    return render(request, 'produto/cadastra_usuario.html', {'form': usuario_form})

def exibe_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form_remove_usuario = RemoveUsuarioForm(initial={'usuario_id': id})
    return render(request, 'produto/exibe_usuario.html', {'usuario': usuario,
                                                          'form_remove_usuario': form_remove_usuario})

def edita_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario_form = UsuarioForm(instance=usuario)
    usuario_form.fields['usuario_id'].initial = id
    return render(request, 'produto/cadastra_usuario.html', {'form': usuario_form })


def remove_usuario(request):
    form_remove_usuario = RemoveUsuarioForm(request.POST)
    if form_remove_usuario.is_valid():
        usuario_id = form_remove_usuario.cleaned_data['usuario_id']
        usuario = get_object_or_404(Usuario, id=usuario_id)
        usuario.delete()

        return render(request, 'produto/exibe_usuario.html', {'usuario': usuario})
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar remover um usuario (usuario_id não foi validado).')



def pesquisa_usuario(request):
    form = PesquisaUsuarioForm()
    return render(request, 'produto/pesquisa_usuario.html', {'form': form})



def exibe_usuarios(request):
    # buscaPor = request.GET.get('buscaPor')
    form = PesquisaUsuarioForm(request.GET)
    if form.is_valid():
        buscaPor = form.cleaned_data['buscaPor']
        lista_de_usuarios = Usuario.objects.filter(nome__contains=buscaPor)
        paginator = Paginator(lista_de_usuarios,5)
        pagina = request.GET.get('pagina')
        usuarios = paginator.get_page(pagina)
    else:
        raise ValueError('Ocorreu um erro inesperado ao pesquisar usuarios.')

    return render(request, 'produto/pesquisa_usuario.html', {'form': form,
                                                             'usuarios': usuarios})



