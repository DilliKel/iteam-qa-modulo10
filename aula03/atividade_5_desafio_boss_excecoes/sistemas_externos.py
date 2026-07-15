# sistemas_externos.py

def cobrar_cartao_api(numero_cartao, valor):
    """Simula a API do Banco que requer internet."""
    print("Conectando ao banco de dados externo...")
    # Se estivesse sem internet, isso lançaria um ConnectionError
    return True 

def alertar_administrador(mensagem_socorro):
    """Simula um envio de SMS/Slack para o time de TI."""
    print(f"ALERTA TI: {mensagem_socorro}")
    return True