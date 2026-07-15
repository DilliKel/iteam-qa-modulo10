# 🧠 Atividade 4: Mocks Inteligentes (Nível Intermediário)

**Objetivo:** Compreender na prática a definição de um Mock. Diferente de um Stub (que só devolve dados), o Mock verifica **o comportamento** do sistema: quantas vezes foi chamado e com quais parâmetros[cite: 14].

## 📖 O Cenário
Você está testando o sistema de finalização de compras de uma loja. A regra de negócio diz o seguinte:
1. Se o cliente tiver saldo suficiente, a compra é aprovada e o sistema **deve enviar um e-mail de confirmação**.
2. Se o cliente **não** tiver saldo, a compra é negada e o sistema **NÃO deve enviar e-mail**.

## 🛠️ O que você deve fazer:
O envio de e-mails de verdade custa dinheiro para a empresa e exige internet. Em nossos testes de unidade com Isolamento Absoluto[cite: 14], não podemos mandar e-mails reais!

1. Abra o arquivo `test_loja.py`. 
2. Você precisará escrever dois testes usando o `@patch` para criar um Mock da função de e-mail.
3. No primeiro teste (Compra com Sucesso), você deve usar o Mock para verificar se a função de e-mail **foi chamada** com os dados corretos (`mock.assert_called_once_with(...)`).
4. No segundo teste (Sem Saldo), você deve garantir que a função de e-mail **NUNCA foi chamada** (`mock.assert_not_called()`).

---
*Dica: Travou? Consulte a pasta `gabarito/respostas.md`.*