# calculadora.py
def calcular_desconto_combo(valor_total, tipo_cliente):
    # Caminho 1: Valor inválido
    if valor_total <= 0:
        raise ValueError("O valor total deve ser maior que zero")
        
    # Caminho 2: Cliente VIP
    if tipo_cliente == "VIP":
        return valor_total * 0.20  # 20% desconto
        
    # Caminho 3: Cliente PREMIUM
    elif tipo_cliente == "PREMIUM":
        return valor_total * 0.10  # 10% desconto
        
    # Caminho 4: Cliente normal
    return 0.0  # Sem desconto para clientes normais