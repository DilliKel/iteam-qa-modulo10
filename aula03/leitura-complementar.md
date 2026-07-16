# Leitura Complementar — Qualidade de Software e Fundamentos de Teste na Profissão de QA

**Fonte:** Prof. Felipe Túlio de Castro — [felipetulio.com.br](https://felipetulio.com.br/qualidade-de-software-e-fundamentos-de-teste-na-profissao-de-qa/) (28/05/2026)
**Compartilhado pelo professor durante a Aula 03.**

## 1. A evolução da profissão de QA

O papel deixou de ser o de "testador tradicional" (execução manual, registro de defeitos depois que o código já está pronto) para o de **Analista de Quality Assurance**: alguém que participa desde a concepção do produto, discute critérios de aceite, antecipa riscos e automatiza verificações — em vez de só reagir a bugs no final.

## 2. O que é qualidade de software

Segundo Pressman e Maxim (2020), qualidade é "conformidade com requisitos explícitos e padrões documentados", mais características implícitas como manutenibilidade, confiabilidade e usabilidade — ou seja, não é só "funcionar", é funcionar do jeito certo, de forma sustentável.

**Custo das falhas (Boehm, 1981):** quanto mais tarde um defeito é encontrado no ciclo de vida, mais caro ele fica para corrigir — o mesmo princípio que já vimos na [Aula 01](../aula01/exercicios-fixacao.md#3-por-que-o-custo-de-correção-de-um-bug-cresce-na-fase-de-produção).

### Atributos de qualidade (ISO/IEC 25010)

| Externos (o usuário percebe) | Internos (estrutura técnica) |
|---|---|
| Adequação funcional | Clareza do código |
| Eficiência de desempenho | Modularidade |
| Compatibilidade | Testabilidade |
| Usabilidade | Organização arquitetural |
| Confiabilidade | Facilidade de manutenção |
| Segurança | |

## 3. Fundamentos de teste

### Caixa-Preta vs. Caixa-Branca

Confirma exatamente o que praticamos na [Atividade 3 da Aula 02](../aula02/atividade_3_caixa_preta_branca/):

- **Caixa-Preta (funcional):** avalia o comportamento observável do sistema, sem exigir conhecimento da implementação. Técnicas citadas: particionamento de equivalência, análise de valor limite, tabelas de decisão.
- **Caixa-Branca (estrutural):** considera caminhos de execução, decisões condicionais e laços; avalia cobertura de instruções e ramos. Especialmente útil em testes unitários — exatamente o que fizemos ao cobrir os 3 `if`/`return` do `pix.py`.

### Pirâmide de testes (níveis)

```
        Testes de Sistema     ← poucos, caros, fluxos completos de negócio
      Testes de Integração    ← interação entre módulos/serviços/APIs
    Testes Unitários (base)   ← muitos, rápidos, unidades isoladas
```

Quanto mais alto na pirâmide, menos testes você deve ter (são mais lentos e caros) — a base larga de testes unitários é o que dá velocidade e segurança para o time.

## 4. Testes unitários e isolamento — a base da Aula 03

Um bom teste unitário deve ser:

- **Determinístico** — mesmo resultado sempre, sob as mesmas condições.
- **Legível** — expressa claramente cenário, ação e resultado esperado.
- **Rápido** — dá para rodar dezenas de vezes por dia sem incomodar.
- **Independente** — não depende de ordem de execução, rede ou serviços externos.

Isso é literalmente o conceito de **Isolamento Absoluto** que abre o [README da Aula 03](README.md).

### Test Doubles (Meszaros, 2007)

O artigo confirma a distinção que já praticamos nas atividades 3, 4 e 5, e ainda acrescenta um terceiro tipo:

1. **Stub** — fornece respostas pré-definidas/fixas para a unidade testada (usamos em [`test_calculadora_nuvem.py`](atividade_3_mock_e_stub/test_calculadora_nuvem.py), com `mock_consultar.return_value = "VIP"`).
2. **Mock** — verifica *interações*: confirma se métodos foram chamados, quantas vezes, e com quais parâmetros (usamos em [`test_loja.py`](atividade_4_mocks_inteligentes/test_loja.py) e [`test_checkout.py`](atividade_5_desafio_boss_excecoes/test_checkout.py), com `assert_called_once_with` / `assert_not_called`).
3. **Fake** — implementação simplificada, mas ainda funcional (ex: um banco de dados em memória no lugar do banco real). Não usamos esse tipo ainda nas atividades, mas é bom já reconhecer o nome.

## 5. QA na cultura ágil

- **Atuação contínua:** o QA participa desde o refinamento das histórias, questionando requisitos ambíguos e propondo critérios de aceite — antes mesmo do código existir.
- **BDD (Behavior-Driven Development, North 2006):** formato padrão para descrever comportamento esperado, reduzindo ambiguidade entre negócio e implementação:

  > Dado [contexto], quando [ação], então [resultado]

  Exemplo do artigo: *"Dado aluno com mensalidades atrasadas, quando emitir declaração, então sistema informa pendências financeiras."*

- **Responsabilidade compartilhada:** qualidade não é só "trabalho do QA" — é de todo o time. O QA mantém a disciplina visível e questiona riscos, mas todos contribuem.

## 6. Competências esperadas de um QA

- **Técnicas:** engenharia de software, níveis/técnicas de teste, automação, CI/CD, APIs, banco de dados, noções de arquitetura.
- **Analíticas:** identificação de riscos, decomposição de requisitos, priorização de testes.
- **Comunicacionais:** diálogo constante com negócio, desenvolvimento, produto, design e operações.

## Conclusão do artigo

Um bom QA "pensa sistemicamente" — conecta requisitos, código, experiência do usuário, segurança e entrega. Em mercados de ciclos curtos, qualidade deixa de ser uma etapa isolada no fim do processo e passa a ser **cultura técnica**, presente do início ao fim do desenvolvimento.

## Referências citadas no artigo

Pressman & Maxim (2020) · ISO/IEC 25010 (2011, 2023) · Sommerville (2016) · Beck (2003, TDD) · Crispin & Gregory (2009, Agile Testing) · Martin (2009, Clean Code) · Meszaros (2007, Test Patterns) · Boehm (1981) · North (2006, BDD)
