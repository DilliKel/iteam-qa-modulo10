# servicos.py
def enviar_email_confirmacao(email_cliente, valor):
    """
    Função real que conecta num servidor SMTP (Gmail, AWS, etc) 
    e envia um e-mail. Não queremos executar isso nos testes unitários!
    """
    print(f"Enviando e-mail real para {email_cliente} cobrando R$ {valor}...")
    # Código complexo de rede estaria aqui
    return True