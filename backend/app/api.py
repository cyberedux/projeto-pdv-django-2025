from ninja import NinjaAPI, ModelSchema

from app.models import (
    Produto, 
    Categoria, 
    Venda, 
    FormaDePagamento, 
    ProdutoVendido
)

from app.schemas import *

api = NinjaAPI()

@api.get("/produtos", response=list[ProdutoJSON])
def get_produtos(request):
    """
    Obtem a lista de Produtos
    """
    # equivalente ao SELECT * FROM Produto
    produtos = Produto.objects.all()
    return produtos

@api.get("/categorias", response=list[CategoriaJSON])
def get_categorias(request):
    """
    Obtem a lista de Categorias
    """
    # SELECT * FROM Categoria
    categorias = Categoria.objects.all()
    return categorias

@api.get("/vendas", response=list[VendaJSON])
def get_vendas(request):
    vendas = Venda.objects.all()
    return vendas

@api.get("/formasDePagamento", response=list[FormaDePagamentoJSON])
def get_formasDePagamento(request):
    formas = FormaDePagamento.objects.all()
    return formas


@api.post("/vendas")
def post_venda(request, payload: PostVendaJSON):
    produtos_vendidos = payload.produtos
    id_formaDePagamento = payload.formaDePagamento

    # SELECT * FROM FormaDePagamento WHERE id=id_formaDePagamento
    obj_formaPgto = FormaDePagamento.objects.get(id=id_formaDePagamento)

    obj_venda = Venda.objects.create(
        formaDePagamento=obj_formaPgto,
        total=0
    )

    total_da_compra = 0

    for produto_vendido in produtos_vendidos:
        id_produto = produto_vendido.id
        qntd_produto = produto_vendido.quantidade

        # SELECT * FROM Produto WHERE id=id_produto
        obj_produto = Produto.objects.get(id=id_produto)

        obj_produto_vendido = ProdutoVendido.objects.create(
            produto=obj_produto,
            quantidade=qntd_produto,
            total=qntd_produto*obj_produto.valor,
            venda=obj_venda
        )

        total_da_compra += qntd_produto*obj_produto.valor

    obj_venda.total = total_da_compra
    obj_venda.save()

