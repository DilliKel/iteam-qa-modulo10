# 📦 Atividade 3: Teste de Caixa Preta vs. Caixa Branca

**Objetivo:** Aplicar os conceitos de teste de "Caixa Preta" (foco nas entradas e saídas esperadas) e "Caixa Branca" (foco na estrutura interna e caminhos lógicos do código) num cenário do mundo real.

## 📖 O Cenário
Vocês foram contratados como Analistas de Qualidade (QA) para testar a nova funcionalidade de **Transferência Pix** do banco.

**Regras de Negócio (Especificação):**
1. O valor da transferência não pode ser zero nem negativo.
2. O cliente precisa ter saldo igual ou superior ao valor que deseja transferir.
3. Se as duas condições acima forem cumpridas, a transferência é realizada.

## 🛠️ O que deve fazer:

### Parte A: Teste de Caixa Preta (Olhando de Fora)
Esqueça que o código existe. Baseando-se **apenas** nas Regras de Negócio acima, abra o ficheiro `tabela_testes.md` e preencha a coluna "Resultado Esperado" para cada um dos três cenários.

### Parte B: Teste de Caixa Branca (Olhando de Dentro)
Agora, vamos analisar a estrutura interna! 
1. Abra o ficheiro `pix.py`. 
2. Analise os blocos `if`. Quantos "caminhos lógicos" diferentes o sistema pode tomar? (Ou seja, de quantas formas diferentes a função pode terminar com um `return`?).
3. No final do ficheiro `pix.py`, escreva linhas de código (`print`) para testar **todos** os caminhos lógicos possíveis, garantindo que o seu teste passa por todas as partes do código.

---