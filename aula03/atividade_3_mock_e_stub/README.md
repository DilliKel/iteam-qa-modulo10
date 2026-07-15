# 🕵️‍♂️ Atividade 3: Missão Isolamento (Mocks e Stubs)

**Objetivo:** Usar dublês de testes para simular a resposta de um serviço externo que requer internet.

## 📖 O Cenário
A nossa calculadora evoluiu. Agora, para descobrir o tipo do cliente, precisamos consultar uma API externa na nuvem usando o CPF do usuário[cite: 14]. 
**Problema:** Se a internet cair, o nosso teste vai falhar! O teste deixou de ser isolado.

## 🛠️ O que você deve fazer:
Se a nossa função precisa de dados externos, nós fingimos que esses dados existem usando dublês[cite: 14]. Usaremos um **Stub**, um objeto que retorna uma resposta estática e pré-configurada para o teste avançar[cite: 14].

1. Analise o arquivo `api_cliente.py` (a simulação da nossa internet).
2. Tente rodar os testes no arquivo `test_calculadora_nuvem.py`. Eles vão demorar e falhar se houver lentidão!
3. Substitua a chamada real usando a biblioteca nativa `unittest.mock` (já importada no arquivo de teste) para blindar a nossa suíte[cite: 14]. 

Confira a pasta `gabarito` para ver como usar o `@patch`!