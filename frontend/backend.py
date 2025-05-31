import requests

# HOST_BACKEND = 'http://192.168.15.74:8000'
HOST_BACKEND = 'http://localhost:8000' # localhost

def get_backend(caminho):
    url = HOST_BACKEND + caminho
    resposta = requests.get(url)

    return resposta.json()

def post_backend(caminho, payload_json):
    url = HOST_BACKEND + caminho
    resposta = requests.post(url, json=payload_json)

    return resposta.json()

def get_produtos():
    # 'http://192.168.15.74:8000/api/produtos'
    return get_backend('/api/produtos')

def get_vendas():
    return get_backend('/api/vendas')

def get_formasDePagamento():
    return get_backend('/api/formaDePagamento')

def get_categorias():
    return get_backend('/api/categorias')

def post_venda(payload_json):
    return post_backend('/api/venda', payload_json)