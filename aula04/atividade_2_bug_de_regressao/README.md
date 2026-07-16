# 🐛 Atividade 2: O Bug de Regressão

**Objetivo:** Vivenciar na prática como uma alteração "inofensiva" em um lugar do código pode quebrar o sistema inteiro (Regressão) e como o teste automatizado nos salva disso!

## 📖 O Cenário
O sistema de pedidos está funcionando perfeitamente. Porém, o Gerente do projeto pediu uma refatoração (melhoria de código): 
> *"A função `salvar_pedido` no Banco de Dados tem um nome muito genérico. Por favor, mude o nome dessa função para `registrar_pedido`".*

O desenvolvedor júnior vai lá e altera o nome no Banco de Dados. Mas ele se esquece de que o `ServicoPedidos` dependia daquele nome antigo!

## 🛠️ Passo a Passo da Missão:

**Passo 1: Verificando se está tudo bem (Sinal Verde)**
Abra o terminal nesta pasta e rode o comando:
`pytest test_regressao.py`
*Você verá que o teste vai passar (verde). O sistema atual funciona!*

**Passo 2: Inserindo o Bug acidentalmente**
1. Abra o arquivo `sistema_pedidos_v2.py`.
2. Vá até a linha 8, na classe `BancoDadosFicticio`.
3. Altere o nome da função de `def salvar_pedido(...)` para `def registrar_pedido(...)`.
4. Salve o arquivo.

**Passo 3: A Regressão acontece! (Sinal Vermelho)**
Rode o teste novamente no terminal:
`pytest test_regressao.py`
*BOOM! O teste falhou. Você verá um `AttributeError`. O código que funcionava antes, agora quebrou porque a integração entre o Banco e o Serviço foi destruída.*

**Passo 4: Consertando o Bug**
1. Volte no arquivo `sistema_pedidos_v2.py`.
2. Desça até a classe `ServicoPedidos` (linha 25).
3. Atualize o código para chamar a nova função `registrar_pedido` ao invés da antiga `salvar_pedido`.
4. Rode `pytest` de novo e garanta que ficou verde!