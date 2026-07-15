# test_calculadora.py
import pytest
from calculadora import calcular_desconto_combo

def test_desconto_cliente_vip():
    assert calcular_desconto_combo(100, "VIP") == 20.0

def test_desconto_cliente_premium():
    assert calcular_desconto_combo(100, "PREMIUM") == 10.0

def test_cliente_regular_sem_desconto():
    assert calcular_desconto_combo(100, "REGULAR") == 0.0

def test_valor_invalido_deve_lancar_erro():
    # O pytest verifica se o erro ValueError foi disparado corretamente
    with pytest.raises(ValueError, match="O valor total deve ser maior que zero"):
        calcular_desconto_combo(-50, "VIP")