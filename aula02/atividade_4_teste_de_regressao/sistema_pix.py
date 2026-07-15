def transferir_pix_v2(saldo_conta, valor_transferencia, limite_diario):
    # NOVA REGRA: Verifica o limite diário primeiro
    if valor_transferencia > limite_diario:
        return "Erro: Limite diário excedido"
        
    # REGRAS ANTIGAS: O desenvolvedor mexeu aqui sem querer!
    if valor_transferencia < 0: # <-- Atenção aqui!
        return "Erro: Valor inválido"
    
    if valor_transferencia > saldo_conta:
        return "Erro: Saldo insuficiente"
        
    return "Sucesso: Transferência realizada"

# --- BATERIA DE TESTES DE REGRESSÃO ---
print("--- Rodando Testes Antigos ---")
print("Teste 1 (Pix Válido):", transferir_pix_v2(500, 100, 1000)) # Esperado: Sucesso
print("Teste 2 (Sem Saldo) :", transferir_pix_v2(50, 200, 1000))  # Esperado: Erro: Saldo insuficiente
print("Teste 3 (Valor Zero):", transferir_pix_v2(100, 0, 1000))   # Esperado: Erro: Valor inválido

print("\n--- Rodando Teste Novo (Limite Diário) ---")
print("Teste 4 (Acima Limite):", transferir_pix_v2(5000, 1500, 1000)) # Esperado: Erro: Limite diário excedido