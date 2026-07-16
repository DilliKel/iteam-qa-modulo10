# 🤝 Atividade 1: A Integração Real

**Objetivo:** Escrever um teste de integração que valide se o Serviço de Pedidos consegue se comunicar corretamente com o Banco de Dados.

## 🛠️ O que você deve fazer:
1. Abra o arquivo `sistema_pedidos.py`. Nele temos duas classes reais: o `BancoDadosFicticio` e o `ServicoPedidos`.
2. Abra o arquivo `test_sistema_pedidos.py`. O código de teste já está lá, mas você precisa entender como ele funciona.
3. Repare que **não estamos usando @patch (Mock)**. Nós instanciamos o banco real e o passamos para o serviço!
4. Rode `pytest` no terminal dentro desta pasta. O teste deve passar.
5. Responda mentalmente: Como o teste garante que o dado realmente foi parar no banco de dados? *(Dica: Olhe a última linha do teste).*