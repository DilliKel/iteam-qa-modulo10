# Exercícios de Fixação — Aula 03 (Dia 3)

## 1. Novos cenários de teste para a regra "clientes antigos (+2 anos) recebem 5% de desconto"

Antes de escrever os testes, é preciso resolver uma ambiguidade na regra de negócio: **o desconto de 5% se acumula com o desconto de VIP/PREMIUM, ou só se aplica a clientes REGULAR?** Essa pergunta precisa ser respondida pelo time de negócio antes da implementação — é exatamente o tipo de interpretação incompleta que vira um "Erro" (no sentido de [Erro/Defeito/Falha](../aula02/RESPOSTAS.md)) se o desenvolvedor simplesmente assumir uma das duas opções sem confirmar.

Assumindo que a nova regra é avaliada de forma independente (mais um `if` na função, sem interferir nos caminhos de VIP/PREMIUM), os novos cenários de Caixa Branca necessários são:

- **Cliente REGULAR com mais de 2 anos de cadastro** → deve receber 5% de desconto (o novo caminho lógico em si).
- **Cliente REGULAR com menos de 2 anos** → deve continuar em 0% (garante que o caminho antigo não foi quebrado — teste de regressão).
- **Valor-limite: cliente com exatamente 2 anos de cadastro** → caso de fronteira clássico (igual ao bug de `> 100` vs. `>= 100` da [Atividade 1 da Aula 02](../aula02/atividade_1_erro_defeito_falha/frete.py)). É preciso testar explicitamente se "mais de 2 anos" inclui ou exclui o valor exato de 2 anos.
- **Cliente VIP/PREMIUM com mais de 2 anos** → um teste para confirmar qual dos dois descontos prevalece (ou se acumulam), validando a decisão tomada na ambiguidade acima.
- **Valor total inválido (`<= 0`)** → não é um caminho novo, mas deve ser re-executado como teste de regressão, garantindo que a nova regra não alterou esse comportamento existente.

## 2. Por que Mocks e Stubs são indispensáveis para um teste ser realmente um Teste de Unidade

Por definição, um teste de unidade valida a lógica de **uma única unidade isolada**, sem depender de fatores externos. Se a função testada chama uma API real, um banco de dados real, ou envia um e-mail de verdade, o resultado do teste passa a depender da disponibilidade, velocidade e correção desses sistemas externos — não apenas da lógica da função em si.

Isso quebra as características que fazem um teste ser confiável (vimos isso na [leitura complementar](leitura-complementar.md)): deixa de ser **determinístico** (a rede pode falhar por motivos alheios ao código), deixa de ser **rápido** (chamadas de rede/banco levam segundos, não milissegundos) e deixa de ser **independente**. Na prática, um teste que depende de um sistema externo real não é mais um teste de unidade — é um **teste de integração** disfarçado.

Mocks e Stubs resolvem isso substituindo a dependência externa por um objeto simulado e controlado pelo próprio teste. Vimos isso na prática nas atividades da Aula 03: o Stub em [`test_calculadora_nuvem.py`](atividade_3_mock_e_stub/test_calculadora_nuvem.py) elimina os 3 segundos de espera de uma API simulada, e os Mocks em [`test_loja.py`](atividade_4_mocks_inteligentes/test_loja.py) e [`test_checkout.py`](atividade_5_desafio_boss_excecoes/test_checkout.py) evitam enviar e-mails reais ou depender de um gateway de pagamento de verdade — inclusive simulando uma falha de conexão (`side_effect = ConnectionError`) que seria praticamente impossível de reproduzir de forma confiável usando o serviço real.

## 3. Palavra-chave/anotação de asserção — pytest

Escolhi o **pytest** (a ferramenta que usamos em toda a Aula 03). Diferente de frameworks como JUnit (`assertEquals(esperado, atual)`) ou Jest (`expect(resultado).toBe(valor)`), o pytest **não tem uma palavra-chave própria de asserção** — ele reaproveita a instrução nativa do Python, `assert`, e usa uma técnica chamada *assertion rewriting* para interceptar essa instrução em tempo de execução e gerar relatórios de falha detalhados (foi exatamente o que vimos na Atividade 2, com o `AssertionError: assert 20.0 == 50.0` mostrando os dois valores comparados).

Isso é uma das razões pelas quais o pytest é descrito como "extremamente legível e sem boilerplate": você escreve `assert calcular_desconto_combo(100, "VIP") == 20.0` como uma expressão comum de Python, em vez de precisar chamar um método especial de asserção.
