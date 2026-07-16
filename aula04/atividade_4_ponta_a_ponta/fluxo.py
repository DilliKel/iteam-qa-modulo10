class BancoReal:
    def __init__(self):
        self.tabela = []
    
    def inserir(self, dado):
        self.tabela.append(dado)

class ControladorHTTP:
    def __init__(self, banco):
        self.banco = banco
        
    def receber_request(self, produto):
        self.banco.inserir(produto)
        return "OK"

class InterfaceUsuario:
    def __init__(self, controlador):
        self.controlador = controlador
        
    def clicar_botao_salvar(self, texto_digitado):
        return self.controlador.receber_request(texto_digitado)