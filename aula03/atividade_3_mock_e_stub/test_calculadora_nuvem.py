import pytest
from unittest.mock import patch
from calculadora_nuvem import calcular_desconto_por_cpf

# ❌ Este teste executa a chamada real da internet (Ruim para testes unitários)
def test_desconto_sem_mock():
    # Vai demorar 3 segundos!
    resultado = calcular_desconto_por_cpf(100, "12345678900")
    assert resultado == 20.0

# ✅ Desafio: Escreva o teste usando Mocks/Stubs abaixo!
# Use o @patch('calculadora_nuvem.consultar_tipo_cliente_na_api')