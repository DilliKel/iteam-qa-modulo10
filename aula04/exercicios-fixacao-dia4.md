# Exercícios de Fixação — Aula 04 (Dia 4)

## 1. Por que a abordagem Big Bang gera alto custo de depuração

No Big Bang, todos os módulos são integrados de uma só vez e o sistema inteiro é testado como um bloco único. Se um defeito aparece, você não tem nenhum ponto de checagem intermediário — o erro pode estar na comunicação entre qualquer par (ou combinação) de módulos, então isolar a causa raiz vira um processo de eliminação manual e demorado, exatamente porque múltiplas integrações novas entraram em produção ao mesmo tempo.

Nas abordagens graduais (Top-Down e Bottom-Up, que praticamos nas [Atividades 3 e 4](atividade_3_top_down/) da Aula 04), você integra um módulo de cada vez, usando Stubs para o que ainda não existe. Quando um teste falha, você sabe que o problema está relacionado à peça que acabou de ser conectada — o espaço de busca do bug fica drasticamente menor, porque tudo que já foi testado nas rodadas anteriores continua confiável.

## 2. Correção de bug no login quebrou o "Esqueci minha senha" — que teste falhou?

O tipo de teste que falhou em prevenir essa situação foi o **Teste de Regressão**. O cenário é exatamente o que vivemos na [Atividade 2 da Aula 04](atividade_2_bug_de_regressao/): uma alteração aparentemente isolada e "inofensiva" (a correção do bug de login) mexeu em algum componente compartilhado — provavelmente uma função ou módulo usado tanto pelo fluxo de login quanto pelo de recuperação de senha — e ninguém rodou a bateria de testes antigos cobrindo o fluxo de "Esqueci minha senha" antes do deploy.

Se existisse (e tivesse sido executada) uma suíte de regressão cobrindo esse segundo fluxo, o teste teria falhado ainda no ambiente de desenvolvimento, antes da mudança chegar em produção — evitando que os usuários fossem os primeiros a descobrir o problema.

## 3. Diferença conceitual: dependência (banco de dados) em Teste de Unidade vs. Teste de Sistema

Em um **Teste de Unidade**, a dependência (o banco de dados) é **simulada** — substituída por um Mock, Stub ou Fake, como fizemos nas atividades da [Aula 03](../aula03/). Nenhuma leitura/escrita real acontece; o comportamento do "banco" é totalmente controlado pelo próprio teste, e o objetivo é validar só a lógica de negócio da unidade, isolada de qualquer efeito colateral externo.

Em um **Teste de Sistema**, a dependência é **real** — o fluxo roda de ponta a ponta contra um banco de dados de verdade (ou uma réplica fiel do ambiente de produção), como fizemos na [Atividade 4 da Aula 04](atividade_4_ponta_a_ponta/) com o `BancoReal`. Aqui o objetivo muda: não é só validar a lógica de negócio, mas também a integridade da persistência em si — se o dado realmente atravessa todas as camadas (interface → controlador → banco) e fica gravado corretamente, incluindo aspectos de rede, schema e comportamento real de I/O que um Mock nunca reproduziria.
