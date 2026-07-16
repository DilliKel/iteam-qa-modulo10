# test_api_posts.py
# Versão em pytest das mesmas requisições/asserções da coleção Bruno (colecao_bruno/),
# para quem preferir rodar via terminal em vez do app Bruno.
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def test_obter_post_real():
    resposta = requests.get(f"{BASE_URL}/1")

    assert resposta.status_code == 200
    assert resposta.json()["userId"] == 1


def test_criar_novo_post():
    payload = {
        "title": "Aula de Testes de API",
        "body": "Aprendendo a usar o Bruno para testes de integracao de API real.",
        "userId": 10,
    }

    resposta = requests.post(BASE_URL, json=payload)

    assert resposta.status_code == 201
    assert resposta.json()["title"] == "Aula de Testes de API"
