# test_checkout.py
import pytest
from unittest.mock import patch
from checkout import processar_pagamento

# Desafio 1: Sucesso. Precisamos de 2 Mocks, pois a função importa 2 sistemas externos!
@patch('checkout.alertar_administrador')
@patch('checkout.cobrar_cartao_api')
def test_pagamento_com_sucesso(mock_cobrar, mock_alerta):
    # 1. Configure o mock_cobrar para retornar True
    
    # 2. Chame a função processar_pagamento
    
    # 3. Faça o assert de "Pagamento Aprovado"
    
    # 4. Garanta que o mock_alerta NÃO foi chamado (assert_not_called)
    pass


# Desafio Boss: Simulando a Queda da API
@patch('checkout.alertar_administrador')
@patch('checkout.cobrar_cartao_api')
def test_pagamento_com_queda_de_servidor(mock_cobrar, mock_alerta):
    # 1. Configure o mock_cobrar para explodir um erro!
    # DICA: mock_cobrar.side_effect = ConnectionError("Offline")
    
    # 2. Chame a função processar_pagamento
    
    # 3. Faça o assert de "Erro: Sistema indisponível no momento"
    
    # 4. Garanta que o mock_alerta FOI chamado uma vez para avisar a TI!
    # DICA: mock_alerta.assert_called_once()
    pass