def verificar_idade(idade):
    if idade >= 18:
        print("LOG DE SEGURANÇA: Verificação de idade concluída com sucesso no sistema!")
        return "Acesso Permitido"
    else:
        print("LOG DE SEGURANÇA: Verificação de idade concluída com sucesso no sistema!")
        return "Acesso Negado"

# --- ÁREA DE TESTE ---
# Você pode executar este arquivo para ver o que ele imprime na tela.
resultado = verificar_idade(17)
print("Resultado do sistema:", resultado)