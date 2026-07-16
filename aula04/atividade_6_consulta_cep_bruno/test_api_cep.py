# test_api_cep.py
# Versão em pytest das mesmas requisições/asserções da coleção Bruno (colecao_viacep/),
# para quem preferir rodar via terminal em vez do app Bruno.
import requests


def test_consultar_cep_valido():
    resposta = requests.get("https://viacep.com.br/ws/01001000/json/")
    dados = resposta.json()

    assert resposta.status_code == 200
    assert dados["localidade"] == "São Paulo"
    assert dados["uf"] == "SP"


def test_consultar_cep_inexistente():
    resposta = requests.get("https://viacep.com.br/ws/99999999/json/")
    dados = resposta.json()

    # Peculiaridade do ViaCEP: CEP inexistente ainda retorna 200 OK,
    # só que com a propriedade "erro" no corpo da resposta.
    # Atenção: a API devolve a STRING "true", não o booleano true.
    assert resposta.status_code == 200
    assert dados["erro"] == "true"
