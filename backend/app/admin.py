from django.contrib import admin

from app.models import Produto, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'categoria', 'custo', 'valor')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
