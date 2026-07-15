# Módulo 10 — Teste e Qualidade de Software

Curso Desenvolvimento Full Stack — ITEAM (Instituto Tecnológico Educacional da Amazônia)
Professor: Bruno Ramalho dos Santos

## Conteúdo do módulo

- [`slides/Aula 01 - Teste e Qualidade Software.pdf`](<slides/Aula 01 - Teste e Qualidade Software.pdf>) — slides da Aula 01: Introdução à Qualidade de Software.
- [`slides/Aula 02 - Teste e Qualidade Software.pdf`](<slides/Aula 02 - Teste e Qualidade Software.pdf>) — slides da Aula 02: Fundamentos e Anatomia dos Testes de Software.
- [`slides/Modelo de Apostila - 2026 - ITEAM.docx.pdf`](<slides/Modelo de Apostila - 2026 - ITEAM.docx.pdf>) — apostila completa do módulo, dividida em 5 capítulos.
- [`aula01/`](aula01/) — código e exercícios da Aula 01.
- [`aula02/`](aula02/) — atividades práticas e exercícios da Aula 02.

## Estrutura da apostila

1. **Capítulo 1** — Introdução à Qualidade de Software (pilares de qualidade, SDLC, ISO 9126/25000, QA vs. QC)
2. **Capítulo 2** — Fundamentos e Anatomia dos Testes de Software (erro, defeito, falha; níveis e tipos de teste; caixa preta/branca)
3. **Capítulo 3** — Testes de Unidade e Integração na Prática (frameworks por linguagem, mocks e stubs)
4. **Capítulo 4** — Integração, Regressão e Validação do Sistema (Big Bang, Top-Down, Bottom-Up, testes de sistema E2E)
5. **Capítulo 5** — Automação de Testes, Experiência do Usuário e CI/CD (UI, API, pipelines)

Cada capítulo tem exercícios de fixação (Dias 1 a 5).

## Aula 01 — Mão na Massa

Pasta: [`aula01/`](aula01/)

- [`performance.py`](aula01/performance.py) — identifica violações dos pilares de Eficiência e Manutenibilidade em tempo de execução, comparando um algoritmo de busca ineficiente O(N²) com uma versão otimizada O(N).
- [`exercicios-fixacao.md`](aula01/exercicios-fixacao.md) — respostas dos exercícios de fixação do Capítulo 1 (QA vs. QC, pilares de qualidade, custo de correção de bugs).

Como executar:

```bash
python aula01/performance.py
```

O script roda as duas versões (ineficiente e otimizada), valida que ambas produzem o mesmo resultado e imprime o ganho de performance obtido ao eliminar o laço interno.

## Aula 02 — Laboratório Prático: Fundamentos de Teste e Qualidade de Software

Pasta: [`aula02/`](aula02/) — veja o [README da aula](aula02/README.md) para o enunciado completo das 4 missões.

- [`atividade_1_erro_defeito_falha/`](aula02/atividade_1_erro_defeito_falha/) — caça ao Erro, Defeito e Falha num bug de cálculo de frete.
- [`atividade_2_codigo_morto/`](aula02/atividade_2_codigo_morto/) — identificação e correção de código morto num sistema de login.
- [`atividade_3_caixa_preta_branca/`](aula02/atividade_3_caixa_preta_branca/) — testes de caixa preta e caixa branca numa transferência Pix.
- [`atividade_4_teste_de_regressao/`](aula02/atividade_4_teste_de_regressao/) — identificação e correção de uma regressão introduzida numa nova feature de Pix.
- [`RESPOSTAS.md`](aula02/RESPOSTAS.md) — respostas das perguntas reflexivas das atividades acima.
- [`exercicios-fixacao-dia2.md`](aula02/exercicios-fixacao-dia2.md) — respostas dos exercícios de fixação do Capítulo 2, Dia 2.

Como executar cada atividade:

```bash
python aula02/atividade_1_erro_defeito_falha/frete.py
python aula02/atividade_2_codigo_morto/login.py
python aula02/atividade_3_caixa_preta_branca/pix.py
python aula02/atividade_4_teste_de_regressao/sistema_pix.py
```
