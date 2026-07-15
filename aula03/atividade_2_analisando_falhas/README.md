# 🚨 Atividade 2: Lendo Relatórios de Falha

**Objetivo:** Ver o comportamento do `pytest` quando um defeito é introduzido no sistema ou no teste.

## 🛠️ O que você deve fazer:
1. Volte ao seu arquivo `test_calculadora.py` da Atividade 1.
2. Faça um teste falhar de propósito! Altere a linha do VIP para esperar o valor errado. Exemplo: `assert calcular_desconto_combo(100, "VIP") == 50.0`
3. Rode `pytest` no terminal novamente.
4. Analise o relatório em vermelho. Perceba como o `pytest` aponta exatamente a linha que falhou e mostra a diferença entre o valor que a função retornou e o valor que você esperava.
5. Corrija o teste de volta para `20.0` e garanta que ele fique verde novamente.