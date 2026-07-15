def verificar_idade(idade):
    if idade >= 18:
        return "Acesso Permitido"
    else:
        return "Acesso Negado"
        
    # Esta linha deveria salvar um log de segurança no terminal.
    # Por que ela nunca é executada pelo programa?
    print("LOG DE SEGURANÇA: Verificação de idade concluída com sucesso no sistema!")

# --- ÁREA DE TESTE ---
# Você pode executar este arquivo para ver o que ele imprime na tela.
resultado = verificar_idade(20)
print("Resultado do sistema:", resultado)