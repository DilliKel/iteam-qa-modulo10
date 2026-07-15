# 🧟‍♂️ Atividade 2: O Perigo do Código Morto

**Objetivo:** Compreender o conceito de "Código Morto" e como defeitos graves podem ficar escondidos no sistema sem que o usuário perceba, até que seja tarde demais.

## 📖 O Cenário
Você tem um sistema simples de login que verifica se o usuário é maior de idade. O sistema parece funcionar perfeitamente: se o usuário tem 18 anos ou mais, ele entra; se tem menos, o acesso é negado.

No entanto, o auditor de segurança do sistema percebeu uma falha grave: a linha de log que registra a verificação no banco de dados **nunca é executada**, deixando o sistema sem rastreabilidade de quem tentou fazer login.

O código escrito está no arquivo `login.py`.

## 🛠️ O que você deve fazer:
1. Abra o arquivo `login.py` na sua máquina.
2. Execute o código e observe a saída no terminal.
3. Responda (no seu caderno ou em um arquivo de anotações):
   * Onde está o "Código Morto" (a linha que nunca será executada pelo computador) neste arquivo?
   * Por que essa linha nunca é executada? Qual instrução de programação está impedindo o fluxo de chegar até ela?
4. **Corrija o código** no arquivo `login.py` para que a mensagem de log seja impressa no terminal **antes** do sistema retornar a resposta final ao usuário.

---