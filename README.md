# Módulo 10 — Teste e Qualidade de Software

Curso Desenvolvimento Full Stack — ITEAM (Instituto Tecnológico Educacional da Amazônia)
Professor: Bruno Ramalho dos Santos

## Conteúdo do módulo

- [`Aula 01 - Teste e Qualidade Software.pdf`](<Aula 01 - Teste e Qualidade Software.pdf>) — slides da Aula 01: Introdução à Qualidade de Software.
- [`Modelo de Apostila - 2026 - ITEAM.docx.pdf`](<Modelo de Apostila - 2026 - ITEAM.docx.pdf>) — apostila completa do módulo, dividida em 5 capítulos.
- [`aula01-qualidade/`](aula01-qualidade/) — código da atividade prática da Aula 01.

## Estrutura da apostila

1. **Capítulo 1** — Introdução à Qualidade de Software (pilares de qualidade, SDLC, ISO 9126/25000, QA vs. QC)
2. **Capítulo 2** — Fundamentos e Anatomia dos Testes de Software (erro, defeito, falha; níveis e tipos de teste; caixa preta/branca)
3. **Capítulo 3** — Testes de Unidade e Integração na Prática (frameworks por linguagem, mocks e stubs)
4. **Capítulo 4** — Integração, Regressão e Validação do Sistema (Big Bang, Top-Down, Bottom-Up, testes de sistema E2E)
5. **Capítulo 5** — Automação de Testes, Experiência do Usuário e CI/CD (UI, API, pipelines)

Cada capítulo tem exercícios de fixação (Dias 1 a 5).

## Atividade Aula 01 — Mão na Massa

Pasta: [`aula01-qualidade/performance.py`](aula01-qualidade/performance.py)

**Objetivo:** identificar violações dos pilares de Eficiência e Manutenibilidade em tempo de execução, comparando um algoritmo de busca ineficiente O(N²) com uma versão otimizada O(N).

Como executar:

```bash
python aula01-qualidade/performance.py
```

O script roda as duas versões (ineficiente e otimizada), valida que ambas produzem o mesmo resultado e imprime o ganho de performance obtido ao eliminar o laço interno.
