# test_loja.py
import pytest
from unittest.mock import patch
from loja import finalizar_compra

# Desafio 1: Testar o caminho de Sucesso garantindo que o e-mail foi enviado
@patch('loja.enviar_email_confirmacao')
def test_deve_finalizar_compra_e_enviar_email(mock_enviar_email):
    resultado = finalizar_compra(saldo_cliente=500, valor_compra=100, email_cliente="cliente@teste.com")

    assert resultado == "Sucesso: Compra finalizada"
    mock_enviar_email.assert_called_once_with("cliente@teste.com", 100)


# Desafio 2: Testar o caminho de Erro garantindo que o e-mail NÃO foi enviado
@patch('loja.enviar_email_confirmacao')
def test_nao_deve_enviar_email_se_saldo_insuficiente(mock_enviar_email):
    resultado = finalizar_compra(saldo_cliente=50, valor_compra=100, email_cliente="cliente@teste.com")

    assert resultado == "Erro: Saldo insuficiente"
    mock_enviar_email.assert_not_called()