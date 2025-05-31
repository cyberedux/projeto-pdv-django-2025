import streamlit as st

from backend import *

produtos = get_produtos()
formas_pgto = get_formasDePagamento()
# categorias = get_categorias()
# vendas = get_vendas()

st.title("Sistema PDV")

if 'produtos_venda' not in st.session_state:
    st.session_state.produtos_venda = []

produtos_venda = st.session_state.produtos_venda

def formatar_produto(produto):
    return f"{produto['descricao']} - R$ {produto['valor']}"

def formatar_forma_pgto(forma):
    return forma['nome']

produto_selecionado = st.selectbox("Produto", produtos, format_func=formatar_produto)
quantidade = st.number_input("Quantidade", min_value=0.0)

if st.button("Adicionar", use_container_width=True):
    produtos_venda.append({
        'id': produto_selecionado['id'], 
        'descricao': produto_selecionado['descricao'], 
        'quantidade': quantidade
    })

st.dataframe(produtos_venda)

forma_pgto = st.selectbox('Forma de Pagamento', formas_pgto, format_func=formatar_forma_pgto)

if st.button('Efetuar venda', use_container_width=True):
    venda = post_venda({
        'formaDePagamento': forma_pgto['id'],
        'produtos': produtos_venda
    })

    st.success(f"Venda efetuada, total: {venda['total']}")
    st.dataframe(venda)

# st.markdown("## Produtos")
# st.dataframe(produtos)

# st.markdown("## Vendas")
# st.dataframe(vendas)

# st.markdown("## Formas de Pagamento")
# st.dataframe(formas_pgto)

# st.markdown("## Categorias")
# st.dataframe(categorias)

