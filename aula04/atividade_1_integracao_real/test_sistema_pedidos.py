# test_sistema_pedidos.py
from sistema_pedidos import BancoDadosFicticio, ServicoPedidos

def test_integracao_criar_pedido_com_sucesso():
    # 1. Preparação (Instanciamos os componentes reais trabalhando juntos)
    banco_real = BancoDadosFicticio()
    servico = ServicoPedidos(banco_real)
    
    # 2. Ação
    resposta = servico.criar_pedido("N123", "Notebook", 2)
    
    # 3. Validação do contrato de integração
    assert resposta["status"] == "sucesso"
    assert "id" in resposta
    # Garantimos que o serviço realmente enviou os dados para o banco!
    assert banco_real.dados["N123"]["item"] == "Notebook"