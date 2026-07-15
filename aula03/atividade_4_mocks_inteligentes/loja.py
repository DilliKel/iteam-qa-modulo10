# loja.py
from servicos import enviar_email_confirmacao

def finalizar_compra(saldo_cliente, valor_compra, email_cliente):
    # Regra 1: Saldo Insuficiente
    if valor_compra > saldo_cliente:
        return "Erro: Saldo insuficiente"
    
    # Regra 2: Sucesso! Envia o e-mail
    enviar_email_confirmacao(email_cliente, valor_compra)
    return "Sucesso: Compra finalizada"