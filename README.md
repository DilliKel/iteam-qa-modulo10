# Módulo 10 — Teste e Qualidade de Software

Curso Desenvolvimento Full Stack — ITEAM (Instituto Tecnológico Educacional da Amazônia)
Professor: Bruno Ramalho dos Santos

## Conteúdo do módulo

- [`slides/Aula 01 - Teste e Qualidade Software.pdf`](<slides/Aula 01 - Teste e Qualidade Software.pdf>) — slides da Aula 01: Introdução à Qualidade de Software.
- [`slides/Aula 02 - Teste e Qualidade Software.pdf`](<slides/Aula 02 - Teste e Qualidade Software.pdf>) — slides da Aula 02: Fundamentos e Anatomia dos Testes de Software.
- [`slides/Modelo de Apostila - 2026 - ITEAM.docx.pdf`](<slides/Modelo de Apostila - 2026 - ITEAM.docx.pdf>) — apostila completa do módulo, dividida em 5 capítulos.
- [`aula01/`](aula01/) — código e exercícios da Aula 01.
- [`aula02/`](aula02/) — atividades práticas e exercícios da Aula 02.
- [`aula03/`](aula03/) — atividades práticas e exercícios da Aula 03.
- [`aula04/`](aula04/) — atividades práticas e exercícios da Aula 04.
- [`aula05/`](aula05/) — atividades práticas da Aula 05.

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

## Aula 03 — Laboratório Prático: Testes de Unidade e Integração (pytest)

Pasta: [`aula03/`](aula03/) — veja o [README da aula](aula03/README.md) para o enunciado completo das 5 missões.

Pré-requisito: `python -m pip install pytest` (rode sempre com `python -m pytest`, não só `pytest`, pois o executável pode não estar no PATH).

- [`atividade_1_primeiros_testes/`](aula03/atividade_1_primeiros_testes/) — suíte de testes de Caixa Branca cobrindo os 4 caminhos lógicos de uma calculadora de desconto.
- [`atividade_2_analisando_falhas/`](aula03/atividade_2_analisando_falhas/) — leitura de relatórios de falha do pytest (exercício sem código residual).
- [`atividade_3_mock_e_stub/`](aula03/atividade_3_mock_e_stub/) — Stub para isolar uma dependência externa lenta (API simulada).
- [`atividade_4_mocks_inteligentes/`](aula03/atividade_4_mocks_inteligentes/) — Mock para validar comportamento (envio de e-mail de confirmação).
- [`atividade_5_desafio_boss_excecoes/`](aula03/atividade_5_desafio_boss_excecoes/) — múltiplos Mocks e simulação de exceção (`side_effect`) para testar um plano de contingência.
- [`leitura-complementar.md`](aula03/leitura-complementar.md) — anotações de um artigo complementar sobre qualidade de software e fundamentos de teste na profissão de QA.
- [`exercicios-fixacao-dia3.md`](aula03/exercicios-fixacao-dia3.md) — respostas dos exercícios de fixação do Capítulo 3, Dia 3.

Como executar cada atividade:

```bash
cd aula03/atividade_1_primeiros_testes && python -m pytest -v
cd aula03/atividade_3_mock_e_stub && python -m pytest -v
cd aula03/atividade_4_mocks_inteligentes && python -m pytest -v
cd aula03/atividade_5_desafio_boss_excecoes && python -m pytest -v
```

## Aula 04 — Laboratório Prático: Integração, Regressão e Validação do Sistema

Pasta: [`aula04/`](aula04/) — veja o [README da aula](aula04/README.md) para o enunciado completo das 6 missões.

- [`atividade_1_integracao_real/`](aula04/atividade_1_integracao_real/) — teste de integração real entre `ServicoPedidos` e `BancoDadosFicticio`, sem Mocks.
- [`atividade_2_bug_de_regressao/`](aula04/atividade_2_bug_de_regressao/) — simulação de um bug de regressão causado por um refactor incompleto, corrigido nas duas pontas.
- [`atividade_3_top_down/`](aula04/atividade_3_top_down/) — abordagem Top-Down usando um Stub simples para a camada de banco ainda inexistente.
- [`atividade_4_ponta_a_ponta/`](aula04/atividade_4_ponta_a_ponta/) — teste E2E com todas as camadas reais (Interface → Controlador → Banco), sem Mocks.
- [`atividade_5_testes_api_bruno/`](aula04/atividade_5_testes_api_bruno/) — testes de contrato de API reais (JSONPlaceholder), com coleção do [Bruno](https://www.usebruno.com/) e uma versão equivalente em `pytest` + `requests` (`test_api_posts.py`).
- [`atividade_6_consulta_cep_bruno/`](aula04/atividade_6_consulta_cep_bruno/) — mesma ideia contra a API pública do ViaCEP, incluindo o caso de CEP inexistente (`test_api_cep.py`).
- [`exercicios-fixacao-dia4.md`](aula04/exercicios-fixacao-dia4.md) — respostas dos exercícios de fixação do Capítulo 4, Dia 4.

Pré-requisito extra para as atividades 5 e 6: `python -m pip install requests` (necessário só para as versões em pytest; a coleção do Bruno em si roda direto no app **ou** pelo terminal via Bruno CLI — veja abaixo).

Como executar cada atividade:

```bash
cd aula04/atividade_1_integracao_real && python -m pytest -v
cd aula04/atividade_2_bug_de_regressao && python -m pytest -v
cd aula04/atividade_3_top_down && python -m pytest -v
cd aula04/atividade_4_ponta_a_ponta && python -m pytest -v
cd aula04/atividade_5_testes_api_bruno && python -m pytest -v
cd aula04/atividade_6_consulta_cep_bruno && python -m pytest -v
```

### Rodando as coleções do Bruno sem abrir o app (Bruno CLI)

As atividades 5 e 6 foram desenhadas pra usar o app gráfico do [Bruno](https://www.usebruno.com/), mas ele também tem uma versão de linha de comando (`@usebruno/cli`) que roda os mesmos arquivos `.bru`, sem precisar de interface gráfica:

```bash
npm install -g @usebruno/cli

cd aula04/atividade_5_testes_api_bruno/colecao_bruno && bru run
cd aula04/atividade_6_consulta_cep_bruno/colecao_viacep && bru run
```

A saída mostra cada requisição e cada asserção (✓/✕), igual à aba "Assert" do app, mas direto no terminal.

## Aula 05 — Laboratório Prático: Automação de Interface (UI) com Selenium

Pasta: [`aula05/`](aula05/) — veja o [README da aula](aula05/README.md) para o enunciado completo das 4 missões.

Pré-requisito: `python -m pip install pytest selenium` (o Selenium moderno baixa o driver do Chrome automaticamente).

- [`atividade_1_primeiros_passos/`](aula05/atividade_1_primeiros_passos/) — primeiro contato com o Selenium: abrir o navegador e validar o título da aba.
- [`atividade_2_interacao/`](aula05/atividade_2_interacao/) — digitar numa caixa de busca e submeter um formulário na Wikipédia.
- [`atividade_3_formularios/`](aula05/atividade_3_formularios/) — automação de login num e-commerce de testes (SauceDemo).
- [`atividade_4_espera_inteligente/`](aula05/atividade_4_espera_inteligente/) — espera explícita (`WebDriverWait`) para lidar com elementos que carregam de forma assíncrona.
- [`exercicios-fixacao-dia5.md`](aula05/exercicios-fixacao-dia5.md) — respostas dos exercícios de fixação do Capítulo 5, Dia 5.

Como executar cada atividade:

```bash
cd aula05/atividade_1_primeiros_passos && python -m pytest -v
cd aula05/atividade_2_interacao && python -m pytest -v
cd aula05/atividade_3_formularios && python -m pytest -v
cd aula05/atividade_4_espera_inteligente && python -m pytest -v
```

## Dificuldades encontradas ao longo das 5 aulas

Nem tudo foi direto — algumas dessas dificuldades vieram de detalhes sutis do próprio código do curso, outras da natureza do que estava sendo testado:

- **Nomes de arquivo quebrando a automação silenciosamente.** O arquivo `test_regressao.py.py` (Aula 04, Atividade 2) tinha uma extensão duplicada que impedia o `pytest` de sequer importar o módulo — um erro de coleção que não tem nada a ver com lógica de teste, mas que só aparece quando você tenta rodar.
- **Ferramentas instaladas, mas fora do alcance do terminal.** O `pytest.exe` foi instalado via `pip install --user` e não caiu no PATH do Windows — rodar só `pytest` falhava silenciosamente ou não fazia nada; foi preciso usar sempre `python -m pytest`.
- **O contrato real de uma API divergindo do que a documentação/atividade sugeria.** Na Aula 04, o ViaCEP devolve a propriedade `erro` como a **string** `"true"`, não como booleano — um detalhe que só apareceu rodando o teste contra a internet de verdade, tanto em Python quanto no próprio Bruno CLI.
- **Ambiguidade de regra de negócio.** No exercício de fixação da Aula 03 (desconto por antiguidade), a regra não deixava claro se o desconto se acumulava com o de cliente VIP/PREMIUM ou não — um lembrete de que perguntar antes de codificar evita um "Erro" (no sentido de Erro/Defeito/Falha) se transformar em bug.
- **Testes de UI "flaky" (instáveis) na Aula 05** — de longe a dificuldade mais sentida na prática: a janela do Chrome abre pequena por padrão, e isso escondia a barra de busca da Wikipédia por causa do layout responsivo (`ElementNotInteractableException`); depois, mesmo com o elemento visível, o código seguia mais rápido que o carregamento da página, fazendo o `assert` pegar o título antigo. É o ciclo "corrige um passo, quebra em outro" — natural quando se está testando várias camadas (rede, DOM, JavaScript) ao mesmo tempo, não só lógica isolada.
- **Manter o raciocínio numa cadeia longa de dependências.** Nas atividades de integração/E2E (Aula 04) e principalmente nas de UI (Aula 05), um erro pequeno numa etapa anterior (ex: elemento errado, timing errado) se propaga e confunde o diagnóstico do passo seguinte — reforçando por que testes unitários isolados (Aula 03) são tão mais rápidos de depurar.

## Aprendizados das 5 aulas

- **Aula 01 — Fundamentos de qualidade:** a diferença entre QA (processo, preventivo) e QC (produto, reativo); os pilares de qualidade da ISO 9126/25000 (atributos externos como usabilidade e confiabilidade, e internos como manutenibilidade e testabilidade); a curva de custo de correção (quanto mais tarde um bug é achado, mais caro fica); e complexidade algorítmica na prática, comparando um algoritmo O(N²) com um O(N).
- **Aula 02 — Anatomia do bug:** a separação entre Erro (engano humano), Defeito (o bug no código) e Falha (o que o usuário vê); o conceito de código morto (código inalcançável, geralmente por estar depois de um `return`); as técnicas de Caixa Preta (baseada na especificação) e Caixa Branca (baseada nos caminhos lógicos do código); e teste de regressão (garantir que uma mudança nova não quebra o que já funcionava).
- **Aula 03 — Automação e isolamento:** o framework `pytest` na prática; o conceito de Isolamento Absoluto (um teste de unidade não pode depender de rede, banco ou serviços externos); os três tipos de Test Doubles — Stub (resposta fixa), Mock (verifica comportamento/chamadas) e Fake (implementação simplificada mas funcional); e a introdução ao BDD (formato Dado/Quando/Então) como forma de reduzir ambiguidade entre negócio e código.
- **Aula 04 — Integração e validação do sistema:** a diferença entre testar com dependências simuladas (Aula 03) e testar componentes reais conversando entre si; as abordagens de integração Big Bang (arriscada), Top-Down e Bottom-Up; o Teste de Sistema E2E (ponta a ponta, sem nenhum mock); e testes de contrato de API contra serviços reais (JSONPlaceholder, ViaCEP) — e por que validar contra o sistema real às vezes revela surpresas que a documentação não menciona.
- **Aula 05 — Automação de interface:** o Selenium controlando um navegador de verdade; a diferença de velocidade e estabilidade entre testar lógica isolada e testar uma interface completa (rede + DOM + JavaScript); e o conceito de espera explícita (`WebDriverWait`) como a ferramenta certa pra lidar com a principal causa de instabilidade em testes de UI — o código rodando mais rápido do que a tela consegue carregar.

No fim, os 5 assuntos se encaixam numa progressão só: entender o que é qualidade (Aula 01) → entender como um bug nasce e se manifesta (Aula 02) → isolar e automatizar a menor unidade de código (Aula 03) → validar as peças conversando de verdade (Aula 04) → validar o sistema do jeito que um usuário humano realmente o usa (Aula 05). Cada camada é mais lenta e mais frágil que a anterior — e é exatamente por isso que a Pirâmide de Testes recomenda ter muitos testes unitários na base e poucos testes de UI no topo.

## Autor

**Kelvin Araújo Ferreira**
[linkedin.com/in/dillikel](https://linkedin.com/in/dillikel)
