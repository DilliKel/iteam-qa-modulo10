def rota_http_criar_usuario(json_recebido, banco_de_dados):
    """Camada superior (Interface/API) que recebe dados da internet"""
    nome = json_recebido.get("nome")
    
    if not nome:
        return 400, "Erro: Nome obrigatório"
        
    # Integração com a camada inferior
    banco_de_dados.salvar(nome)
    return 201, "Usuário criado"