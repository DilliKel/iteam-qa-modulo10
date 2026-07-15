def calcular_frete(valor_compra):
    # REGRA DE NEGÓCIO: Frete grátis para compras de R$ 100,00 ou mais.
    if valor_compra >= 100:
        return "Frete Grátis"
    else:
        return "Frete: R$ 20,00"

# ============ ÁREA DE TESTE ============
# Você pode executar este arquivo para ver o que ele imprime na tela.
print("Testando compra de R$ 150,00:", calcular_frete(150)) # Esperado: Frete Grátis
print("Testando compra de R$ 50,00 :", calcular_frete(50))  # Esperado: Frete R$ 20
print("Testando compra de R$ 100,00:", calcular_frete(100)) # Esperado: Frete Grátis