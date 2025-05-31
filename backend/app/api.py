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
    
@api.post('/venda', response=VendaJSON)
def post_venda(request, payload: PostVendaJSON):
    id_formaPgto = payload.formaDePagamento

    # SELECT * FROM FormaDePagamento WHERE id=id_formaPgto
    obj_formaPgto = FormaDePagamento.objects.get(
        id=id_formaPgto
    )

    # INSERT INTO Venda (formaDePagamento, total) VALUES (obj_formaPgto, total)
    obj_venda = Venda.objects.create(
        formaDePagamento = obj_formaPgto,
        total = 0.0
    )

    lista_produtos = payload.produtos

    total_venda = 0
    for produto_vendido in lista_produtos:
        # SELECT * FROM Produto WHERE id=produto_vendido.id
        obj_produto = Produto.objects.get(id=produto_vendido.id)
        # INSERT INTO ProdutoVendido (produto, quantidade, total, venda) 
        # VALUES (obj_produto, produto_vendido.quantidade, total_produto, obj_venda)
        total_produto = obj_produto.valor * produto_vendido.quantidade
        obj_produtoVendido = ProdutoVendido.objects.create(
            produto=obj_produto,
            quantidade=produto_vendido.quantidade,
            total=total_produto,
            venda=obj_venda
        )
        total_venda += total_produto
    
    obj_venda.total = total_venda
    obj_venda.save()

    return obj_venda