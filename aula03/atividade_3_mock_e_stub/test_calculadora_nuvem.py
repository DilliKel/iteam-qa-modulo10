import pytest
from unittest.mock import patch
from calculadora_nuvem import calcular_desconto_por_cpf

# ❌ Este teste executa a chamada real da internet (Ruim para testes unitários)
def test_desconto_sem_mock():
    # Vai demorar 3 segundos!
    resultado = calcular_desconto_por_cpf(100, "12345678900")
    assert resultado == 20.0

# ✅ Teste usando Stub: substitui a chamada real por uma resposta estática e instantânea
@patch('calculadora_nuvem.consultar_tipo_cliente_na_api')
def test_desconto_com_stub_cliente_vip(mock_consultar):
    mock_consultar.return_value = "VIP"

    resultado = calcular_desconto_por_cpf(100, "12345678900")

    assert resultado == 20.0


@patch('calculadora_nuvem.consultar_tipo_cliente_na_api')
def test_desconto_com_stub_cliente_regular(mock_consultar):
    mock_consultar.return_value = "REGULAR"

    resultado = calcular_desconto_por_cpf(100, "12345678900")

    assert resultado == 0.0