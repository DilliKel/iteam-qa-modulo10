# test_loja.py
import pytest
from unittest.mock import patch
from loja import finalizar_compra

# Desafio 1: Testar o caminho de Sucesso garantindo que o e-mail foi enviado
# Dica: Use @patch('loja.enviar_email_confirmacao')
def test_deve_finalizar_compra_e_enviar_email():
    # Escreva seu código aqui
    pass

# Desafio 2: Testar o caminho de Erro garantindo que o e-mail NÃO foi enviado
def test_nao_deve_enviar_email_se_saldo_insuficiente():
    # Escreva seu código aqui
    pass