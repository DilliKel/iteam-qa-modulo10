# 🐞 Atividade 1: Caça ao Erro, Defeito e Falha

**Objetivo:** Compreender a diferença prática entre os conceitos de Erro, Defeito e Falha usando um exemplo real de código.

## 📖 O Cenário
Você recebeu uma especificação da equipe de negócios:
> *"O sistema deve conceder frete grátis para compras de valor **igual ou acima** de R$ 100,00. Caso contrário, o frete custa R$ 20,00."*

Um desenvolvedor escreveu o código que está no arquivo `frete.py`. No entanto, os clientes estão reclamando que compraram exatamente R$ 100,00 e o sistema cobrou o frete de R$ 20,00.

## 🛠️ O que você deve fazer:
1. Abra o arquivo `frete.py` na sua máquina.
2. Execute o código e observe os testes que aparecem no terminal.
3. Responda (no seu caderno ou em um arquivo de anotações):
   * **O Erro (Ação Humana):** O que o desenvolvedor pensou ou interpretou de forma incorreta ao ler a regra de negócio?
   * **O Defeito (Bug no Código):** Em qual linha do arquivo `frete.py` o bug está escrito e o que está incorreto nela?
   * **A Falha (Comportamento Visível):** Qual é o comportamento incorreto que o cliente final vê na tela?
4. **Corrija o código** no arquivo `frete.py` para que ele funcione corretamente conforme a regra de negócio.

---