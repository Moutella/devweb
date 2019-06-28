from django.contrib import admin
from .models import Usuario, Categoria, Produto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'categoria']
    search_fields = ('nome', 'categoria')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    search_fields = ['nome']
# Register your models here.

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
