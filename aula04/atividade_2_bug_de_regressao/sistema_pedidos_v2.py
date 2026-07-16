# sistema_pedidos_v2.py

# ==========================================
# CAMADA 1: BANCO DE DADOS
# ==========================================
class BancoDadosFicticio:
    def __init__(self):
        self.dados = {}

    # ALUNO: NO PASSO 2, MUDE O NOME DESTA FUNÇÃO PARA 'registrar_pedido'
    def salvar_pedido(self, id_pedido, dados_pedido):
        if not id_pedido:
            return False
        self.dados[id_pedido] = dados_pedido
        return True


# ==========================================
# CAMADA 2: REGRAS DE NEGÓCIO (SERVIÇO)
# ==========================================
class ServicoPedidos:
    def __init__(self, banco):
        self.banco = banco

    def criar_pedido(self, id_pedido, item, qtd):
        if qtd <= 0:
            return {"status": "erro", "mensagem": "Quantidade inválida"}

        payload = {"item": item, "quantidade": qtd}
        
        # ALUNO: NO PASSO 4, VOCÊ TERÁ QUE ATUALIZAR A LINHA ABAIXO
        # PARA USAR O NOVO NOME DA FUNÇÃO DO BANCO!
        sucesso = self.banco.salvar_pedido(id_pedido, payload)

        if sucesso:
            return {"status": "sucesso", "id": id_pedido}
        return {"status": "erro", "mensagem": "Falha na persistência"}