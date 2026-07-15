def transferir_pix(saldo_conta, valor_transferencia):
    # Caminho lógico 1: Validação de valor nulo ou negativo
    if valor_transferencia <= 0:
        return "Erro: Valor inválido"
    
    # Caminho lógico 2: Validação de saldo
    if valor_transferencia > saldo_conta:
        return "Erro: Saldo insuficiente"
        
    # Caminho lógico 3: Sucesso
    saldo_conta = saldo_conta - valor_transferencia
    return "Sucesso: Transferência realizada"

# --- ÁREA DE TESTE (CAIXA BRANCA) ---
# O seu objetivo é garantir que o sistema passa por todos os 'return' acima.
# Escreva abaixo os seus testes (um exemplo já está feito):

# Exemplo: Forçando o Caminho 1 (Valor inválido)
print("Teste Caminho 1:", transferir_pix(saldo_conta=100, valor_transferencia=0))

# Escreva os seus próximos testes aqui:
# Forçando o Caminho 2 (Saldo insuficiente)
print("Teste Caminho 2:", transferir_pix(saldo_conta=50, valor_transferencia=200))

# Forçando o Caminho 3 (Sucesso)
print("Teste Caminho 3:", transferir_pix(saldo_conta=500, valor_transferencia=100))