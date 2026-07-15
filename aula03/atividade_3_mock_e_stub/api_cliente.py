import time

def consultar_tipo_cliente_na_api(cpf):
    """
    Simula uma requisição lenta e dependente de internet para um banco de dados real.
    Em um teste unitário perfeito, nós NUNCA queremos executar esta função de verdade.
    """
    time.sleep(3) # Simula lentidão da rede
    return "VIP" # Resposta real do servidor