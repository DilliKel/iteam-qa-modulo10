# 🧪 Laboratório Prático: Fundamentos de Teste e Qualidade de Software

Bem-vindos(as) à nossa aula prática! 🚀

Até agora, discutimos na teoria como os times ágeis de alta performance se comunicam e a importância de garantir a qualidade de uma aplicação antes que ela chegue ao cliente final. Hoje, vocês vão colocar a "mão na massa" e ver esses conceitos funcionando em código real!

Neste laboratório, vamos deixar de lado o termo genérico "deu bug" e investigar como os problemas realmente nascem, se manifestam e se escondem dentro dos sistemas. O nosso objetivo é desenvolver a **mentalidade investigativa e analítica** que todo bom desenvolvedor(a) e Analista de Qualidade (QA) precisa ter.

---

## 🗺️ O que vocês vão enfrentar hoje?

O repositório está estruturado em **4 missões sequenciais**. Vocês devem navegar pelas pastas na ordem abaixo:

### 📁 [Atividade 1: Caça ao Erro, Defeito e Falha](./atividade_1_erro_defeito_falha)
* **Conceito:** A anatomia de um problema de software.
* **Missão:** Analisar um sistema de e-commerce onde uma regra de frete grátis foi mal implementada. Vocês precisarão identificar exatamente onde o ser humano errou (Erro), onde isso ficou registrado no código (Defeito) e qual o impacto disso para o usuário (Falha), além de aplicar a correção matemática adequada.

### 📁 [Atividade 2: O Perigo do Código Morto](./atividade_2_codigo_morto)
* **Conceito:** Cobertura de fluxo e códigos inacessíveis.
* **Missão:** Investigar um sistema de login que parece perfeito por fora, mas esconde uma vulnerabilidade: um log de auditoria essencial que nunca é executado porque foi escrito depois de uma instrução de parada (`return`). Vocês vão ressuscitar esse código!

### 📁 [Atividade 3: Caixa Preta e Caixa Branca (PIX)](./atividade_3_caixa_preta_branca)
* **Conceito:** Abordagens de testes estruturais e funcionais.
* **Missão:** Testar uma transferência Pix de duas formas:
    1.  **Caixa Preta:** Sem olhar o código, preenchendo cenários de teste baseados unicamente nas especificações do banco.
    2.  **Caixa Branca:** Olhando para o código interno, identificando todos os caminhos lógicos (estruturas condicionais) e escrevendo testes que passem por cada um deles.

### 📁 [Atividade 4: O Fantasma da Regressão (Desafio Intermediário!)](./atividade_4_teste_de_regressao)
* **Conceito:** Teste de regressão e efeitos colaterais de alterações.
* **Missão:** O banco pediu para adicionar um "limite diário" ao Pix. O desenvolvedor implementou a nova regra, mas acabou quebrando uma das regras antigas (permitindo Pix de R$ 0,00). O seu papel como QA é rodar a bateria de testes, identificar essa regressão e consertar o estrago.

---

## 🚀 Como começar?

1.  **Fork ou Clone:** Faça um *Fork* deste repositório para a sua conta do GitHub ou clone-o na sua máquina local.
2.  **Instalação:** Certifique-se de ter o Python instalado na sua máquina (as atividades usam sintaxe simples de Python para que todos consigam ler e rodar sem dificuldades).
3.  **Execução:** Navegue pelas pastas (`atividade_1` até `atividade_4`), abra o arquivo `README.md` de cada uma delas para ler as instruções detalhadas e execute os arquivos `.py` correspondentes.
4.  **Resolução:** Altere o código, faça os testes passarem e salve os arquivos.
5.  **Gabarito:** Travou ou terminou? Cada atividade possui uma pasta `/gabarito` com a resposta teórica e o código corrigido para você validar a sua linha de raciocínio.

> 💡 **Dica de Ouro:** Tente explicar em voz alta o que você está fazendo para um colega ou para você mesmo (Técnica de Feynman). Explicar a lógica de testes de forma simples é o melhor caminho para consolidar esse conhecimento!

---
*Bom código e excelentes testes!* 🔍💻
