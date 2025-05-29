import streamlit as st
from api_backend import *

categorias = get_categorias()
produtos = get_produtos()
formas_de_pagamento = get_formas_de_pagamento()

st.title("Sistema PDV")

if 'produtos' not in st.session_state:
    st.session_state['produtos'] = []

produtos_venda = st.session_state.produtos

def formatar_produto(produto):
    return f'{produto['descricao']} - R$ {produto['valor']}'

def formatar_forma_pgto(forma):
    return forma['nome']

produto = st.selectbox('Produto', produtos, format_func=formatar_produto)
quantidade = st.number_input('Quantidade', min_value=0.0)

if st.button('Adicionar', use_container_width=True):
    produtos_venda.append({
        'id': produto['id'], 
        'nome': produto['descricao'],
        'quantidade': quantidade
    })

st.markdown("## Produtos")
st.dataframe(produtos_venda)

forma_de_pagamento = st.selectbox("Forma de Pagamento", formas_de_pagamento, format_func=formatar_forma_pgto) 

if st.button("Efetuar venda", use_container_width=True):
    post_venda(
        {
            "formaDePagamento": forma_de_pagamento['id'],
            "produtos": produtos_venda
        }
    )

    produtos_venda.clear()

    st.success("Venda Efetuada!")

# st.markdown("## Categorias")
# st.dataframe(categorias)

# st.markdown("## Formas de Pagamento")
# st.dataframe(formas_de_pagamento)

vendas = get_vendas()
st.markdown("## Vendas")
st.dataframe(vendas)


