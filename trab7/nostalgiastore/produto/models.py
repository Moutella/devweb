from django.db import models
from django.urls import reverse
from django.conf import settings

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='produtos',
                             on_delete=models.DO_NOTHING,
                             null=True)
    # data_cadastramento = models.DateTimeField(auto_now_add=True)
    # data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produto'

    def get_absolute_path(self):
        return reverse('produto:pagina_produto', args=[self.id, self.slug])

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    email = models.CharField(max_length=200, unique=True)
    nascimento = models.DateField(null=True)
    data_cadastro = models.DateField(null=True)
    cpf = models.CharField(max_length=11, unique=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        db_table= 'usuario'

    def __str__(self):
        return self.nome

    def data_cadastro_masc(self):
        return self.data_cadastro.strftime("%d/%m/%Y")
    def data_nasc_masc(self):
        return self.nascimento.strftime("%d/%m/%Y")