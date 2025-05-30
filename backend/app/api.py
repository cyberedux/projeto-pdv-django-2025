from ninja import NinjaAPI

from app.models import (
    Produto,
    Categoria,
    FormaDePagamento,
    Venda,
    ProdutoVendido,
)
from app.schemas import *

api = NinjaAPI()

@api.get('/produtos', response=list[ProdutoJSON])
def get_produtos(request):
    produtos = Produto.objects.all()
    return produtos

@api.get('/categorias', response=list[CategoriaJSON])
def get_categorias(request):
    categorias = Categoria.objects.all()
    return categorias

@api.get('/formaDePagamento', response=list[FormaDePagamentoJSON])
def get_formaDePagamento(request):
    formas = FormaDePagamento.objects.all()
    return formas

@api.get('/vendas', response=list[VendaJSON])
def get_vendas(request):
    vendas = Venda.objects.all()
    return vendas
    

