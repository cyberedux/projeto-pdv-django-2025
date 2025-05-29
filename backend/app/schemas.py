from ninja import Schema, ModelSchema

from app.models import (
    Produto, 
    Categoria, 
    Venda, 
    FormaDePagamento, 
    ProdutoVendido
)

class CategoriaJSON(ModelSchema):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoJSON(ModelSchema):
    class Meta:
        model = Produto
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

class PostProdutoVendaJSON(Schema):
    id: int
    quantidade: float

class PostVendaJSON(Schema):
    formaDePagamento: int
    produtos: list[PostProdutoVendaJSON]

class FormaDePagamentoJSON(ModelSchema):
    class Meta:
        model = FormaDePagamento
        fields = '__all__'



