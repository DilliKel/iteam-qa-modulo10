# test_regressao.py
import pytest
from sistema_pedidos_v2 import BancoDadosFicticio, ServicoPedidos

def test_integracao_nao_pode_quebrar_apos_refatoracao():
    # 1. Preparação (Instanciamos os componentes reais)
    banco_real = BancoDadosFicticio()
    servico = ServicoPedidos(banco_real)
    
    # 2. Ação
    resposta = servico.criar_pedido("N123", "Mouse Gamer", 1)
    
    # 3. Validação do contrato de integração
    assert resposta["status"] == "sucesso", "A integração falhou! O Serviço não conseguiu falar com o Banco."
    assert "id" in resposta
    
    # Valida se o dado realmente foi gravado no banco real
    assert banco_real.dados["N123"]["item"] == "Mouse Gamer"