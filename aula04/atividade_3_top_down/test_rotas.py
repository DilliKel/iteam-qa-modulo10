import pytest
from api import rota_http_criar_usuario

# 1. Crie o seu Stub aqui!
class BancoStub:
    # Crie o método salvar() que não faz nada, apenas passa!
    pass 

def test_rota_http_com_stub():
    # 2. Instancie seu Stub
    banco_falso = ... 
    
    # 3. Teste a rota passando o Stub
    # status, resposta = rota_http_criar_usuario({"nome": "Bruno"}, banco_falso)
    
    # 4. Crie os Asserts para garantir que retornou 201 e "Usuário criado"
    pass