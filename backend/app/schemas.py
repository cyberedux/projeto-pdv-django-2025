from ninja import ModelSchema, Schema

from app.models import (
    Produto,
    Categoria,
    FormaDePagamento,
    Venda,
    ProdutoVendido,
)

class ProdutoJSON(ModelSchema):
    class Meta:
        model = Produto
        fields = '__all__'
        exclude = ('custo', )

class CategoriaJSON(ModelSchema):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormaDePagamentoJSON(ModelSchema):
    class Meta:
        model = FormaDePagamento
        fields = '__all__'

class ProdutoVendidoJSON(ModelSchema):
    class Meta:
        model = ProdutoVendido
        fields = '__all__'

class VendaJSON(ModelSchema):
    produtos_vendidos: list[ProdutoVendidoJSON]
    class Meta:
        model = Venda
        fields = '__all__'

class PostProdutoVendidoJSON(Schema):
    id: int # id de Produto
    quantidade: float 

class PostVendaJSON(Schema):
    formaDePagamento: int # id de FormaDePagamento
    produtos: list[PostProdutoVendidoJSON]
