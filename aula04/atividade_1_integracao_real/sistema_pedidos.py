# sistema_pedidos.py

class BancoDadosFicticio:
    def __init__(self):
        self.dados = {}

    def salvar_pedido(self, id_pedido, dados_pedido):
        if not id_pedido:
            return False
        self.dados[id_pedido] = dados_pedido
        return True

class ServicoPedidos:
    def __init__(self, banco):
        self.banco = banco

    def criar_pedido(self, id_pedido, item, qtd):
        # Regra de negócio
        if qtd <= 0:
            return {"status": "erro", "mensagem": "Quantidade inválida"}

        payload = {"item": item, "quantidade": qtd}
        # Comunicação de Integração:
        sucesso = self.banco.salvar_pedido(id_pedido, payload)

        if sucesso:
            return {"status": "sucesso", "id": id_pedido}
        return {"status": "erro", "mensagem": "Falha na persistência"}