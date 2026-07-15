# 🧪 Aula 03: Testes de Unidade e Integração na Prática

Bem-vindos(as) a mais um laboratório prático! 🚀

Na aula anterior, entendemos a diferença entre Erro e Falha, e aprendemos a mapear cenários de testes (Caixa Preta e Branca). Hoje, vamos automatizar esse processo!

O nosso objetivo hoje é alcançar o **Isolamento Absoluto**. Uma unidade de código (função ou classe) deve ser a menor parte testável do sistema e seus testes não podem depender de fatores externos, como internet, banco de dados ou arquivos. Isso garante um design limpo e nos dá segurança para refatorar o código sem medo de quebrar regras de negócio.

Para isso, usaremos a linguagem Python com o framework **pytest**, famoso no mercado por ser altamente legível, direto e sem código repetitivo (boilerplate).

## 🗺️ As Missões de Hoje:

1. **[Atividade 1: Primeiros Passos com pytest](./atividade_1_primeiros_testes):** Vamos instalar o framework e rodar nossa primeira suíte de testes de Caixa Branca focada em múltiplos caminhos lógicos.
2. **[Atividade 2: Analisando Falhas](./atividade_2_analisando_falhas):** Vamos quebrar os testes de propósito para entender como o framework nos avisa sobre os bugs.
3. **[Atividade 3: Missão Isolamento (Mocks e Stubs)](./atividade_3_mock_e_stub):** Nossa função agora depende de uma API externa. Como testar se a internet cair? Usaremos dublês de testes para simular essas conexões.
4. **[Atividade 4: Mocks Inteligentes (Nível Intermediário)](./atividade_4_mocks_inteligentes):** Diferente de um Stub que só devolve dados, você vai usar um Mock para validar o **comportamento** do sistema (garantindo que e-mails sejam enviados ou bloqueados nas horas certas).
5. **[Atividade 5: Desafio Boss - O Caos das Exceções (Nível Difícil)](./atividade_5_desafio_boss_excecoes):** O que acontece quando a internet falha e a API sai do ar? Vocês vão empilhar múltiplos Mocks e simular falhas de conexão para garantir que o plano de contingência (avisar a TI) funciona perfeitamente!

## 🚀 Preparação (Pré-requisitos)
Abra o seu terminal no VS Code e instale o framework de testes executando o comando:
`pip install pytest`

Vamos aos códigos! 💻🔍