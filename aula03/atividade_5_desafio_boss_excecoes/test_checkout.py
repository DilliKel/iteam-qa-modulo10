# test_checkout.py
import pytest
from unittest.mock import patch
from checkout import processar_pagamento

# Desafio 1: Sucesso. Precisamos de 2 Mocks, pois a função importa 2 sistemas externos!
@patch('checkout.alertar_administrador')
@patch('checkout.cobrar_cartao_api')
def test_pagamento_com_sucesso(mock_cobrar, mock_alerta):
    # 1. Configure o mock_cobrar para retornar True
    mock_cobrar.return_value = True

    # 2. Chame a função processar_pagamento
    resultado = processar_pagamento("1234-5678-9012-3456", 150.0)

    # 3. Faça o assert de "Pagamento Aprovado"
    assert resultado == "Pagamento Aprovado"

    # 4. Garanta que o mock_alerta NÃO foi chamado (assert_not_called)
    mock_alerta.assert_not_called()


# Desafio Boss: Simulando a Queda da API
@patch('checkout.alertar_administrador')
@patch('checkout.cobrar_cartao_api')
def test_pagamento_com_queda_de_servidor(mock_cobrar, mock_alerta):
    # 1. Configure o mock_cobrar para explodir um erro!
    # DICA: mock_cobrar.side_effect = ConnectionError("Offline")
    mock_cobrar.side_effect = ConnectionError("Banco fora do ar")

    # 2. Chame a função processar_pagamento
    resultado = processar_pagamento("1234-5678-9012-3456", 150.0)

    # 3. Faça o assert de "Erro: Sistema indisponível no momento"
    assert resultado == "Erro: Sistema indisponível no momento"

    # 4. Garanta que o mock_alerta FOI chamado uma vez para avisar a TI!
    # DICA: mock_alerta.assert_called_once()
    mock_alerta.assert_called_once()