from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table='categoria'

    def get_absolute_path(self):
        return reverse('produto:lista_categoria', args=[self.slug])

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    # data_cadastramento = models.DateTimeField(auto_now_add=True)
    # data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produto'

    def get_absolute_path(self):
        return reverse('produto:pagina_produto', args=[self.id, self.slug])

    def __str__(self):
        return self.nome