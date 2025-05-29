import requests

HOST_BACKEND = 'http://192.168.15.74:8000'

def get_backend(caminho):
    url = HOST_BACKEND + caminho
    resposta = requests.get(url)

    return resposta.json()

def post_backend(caminho, payload_json):
    url = HOST_BACKEND + caminho
    resposta = requests.post(url, json=payload_json)

    return resposta.json()

def get_produtos():
    return get_backend('/api/produtos')

def get_categorias():
    return get_backend('/api/categorias')

def get_vendas():
    return get_backend('/api/vendas')

def get_formas_de_pagamento():
    return get_backend('/api/formasDePagamento')

def post_venda(payload_json):
    post_backend('/api/vendas', payload_json)
