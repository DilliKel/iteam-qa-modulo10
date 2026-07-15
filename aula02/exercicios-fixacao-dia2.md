# Exercícios de Fixação — Aula 02 (Dia 2)

## 1. Frete com taxa incorreta — Erro, Defeito e Falha

**Cenário:** o desenvolvedor digitou um valor de taxa de frete incorreto no código; o usuário tentou comprar, o site apresentou o valor errado e a compra foi cancelada.

- **Erro (ação humana):** o desenvolvedor se enganou ao digitar a taxa de frete — seja por não conferir o valor correto na especificação, por um erro de digitação, ou por copiar um valor desatualizado de outra parte do sistema.
- **Defeito (bug no código):** a linha/variável onde o valor numérico incorreto da taxa está escrito no código-fonte (ex: uma constante `TAXA_FRETE = 35` quando deveria ser `TAXA_FRETE = 15`). O defeito é esse valor errado gravado no código, que existe ali silenciosamente até ser executado.
- **Falha (comportamento visível):** o cliente final viu um valor de frete diferente do esperado na tela de checkout, considerou o preço abusivo ou inconsistente com o anunciado, e cancelou a compra. A falha é o prejuízo real e observável causado ao usuário — a venda perdida.

## 2. Testar envio de payload para a API da Stripe

Esse é um **teste de integração** (integration test).

**Justificativa:** o objetivo aqui não é validar uma função isolada do seu próprio código (o que seria um teste de unidade), nem simular o sistema inteiro do ponto de vista do usuário final (teste de sistema/E2E). O foco é verificar se a **comunicação entre dois componentes diferentes** — a sua aplicação Node.js e o serviço externo da Stripe — está correta: se o payload é montado no formato esperado pela API, se a autenticação (chaves de API) funciona, se a resposta é interpretada corretamente pelo seu código, e se erros da API externa (cartão recusado, timeout, etc.) são tratados como esperado. Testar a integração entre módulos/serviços (mesmo quando um deles é um serviço de terceiros) é exatamente a definição de teste de integração.

## 3. Caixa Preta vs. Caixa Branca

A diferença central é o que cada técnica enxerga:

- **Caixa Preta:** testa o sistema **sem conhecimento da implementação interna**, olhando apenas para entradas e saídas esperadas, conforme a especificação/regra de negócio. Pergunta: "dado esse input, o sistema entrega o output que o negócio prometeu?"
- **Caixa Branca:** testa o sistema **com conhecimento total do código-fonte**, analisando a estrutura interna (condicionais, laços, caminhos lógicos) para garantir que cada trecho do código seja exercitado por algum teste. Pergunta: "todo caminho possível dentro do código foi executado e validado?"

**Exemplo prático — Caixa Preta:** testar a transferência Pix da Atividade 3 apenas com base nas regras de negócio (valor não pode ser zero/negativo; saldo deve ser suficiente), preenchendo cenários de entrada e saída esperada sem nunca abrir o arquivo `pix.py`.

**Exemplo prático — Caixa Branca:** abrir o `pix.py`, contar que existem 3 caminhos lógicos (`if valor <= 0`, `if valor > saldo`, sucesso) e escrever um teste para cada `if`/`return`, garantindo cobertura de 100% das linhas de código — inclusive de uma condição que talvez nem estivesse descrita explicitamente na especificação de negócio.
