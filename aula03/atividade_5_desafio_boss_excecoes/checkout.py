# checkout.py
from sistemas_externos import cobrar_cartao_api, alertar_administrador

def processar_pagamento(numero_cartao, valor):
    try:
        # Tenta ir na internet cobrar o cartão
        sucesso = cobrar_cartao_api(numero_cartao, valor)
        
        if sucesso:
            return "Pagamento Aprovado"
        else:
            return "Pagamento Recusado"
            
    except ConnectionError:
        # Plano de contingência: O Banco caiu!
        alertar_administrador("URGENTE: Gateway de pagamento offline!")
        return "Erro: Sistema indisponível no momento"