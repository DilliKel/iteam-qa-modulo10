# 📡 Atividade 5: Testes de Integração de API com Bruno (usebruno.com)

**Objetivo:** Realizar testes de integração reais enviando requisições HTTP para uma API pública na internet (JSONPlaceholder) e automatizar asserções de teste de contrato (como códigos de status e formatos de resposta).

## 📖 O Cenário
Nós integramos nosso sistema de postagens com um serviço externo de terceiros (uma API REST de posts). Precisamos garantir que esse serviço externo está respondendo de acordo com o combinado (contrato de integração):
1. A rota para buscar um post pelo ID deve retornar o código HTTP `200 OK` e dados válidos.
2. A rota para criar um post deve aceitar novos dados e responder com `201 Created`.

Usaremos o **Bruno**, uma ferramenta de API moderna, de código aberto e que salva suas requisições como arquivos simples, facilitando o uso com Git e GitHub!

---

## 🛠️ Passo a Passo da Missão

### Passo 1: Instalação do Bruno
1. Acesse [usebruno.com](https://www.usebruno.com/) e faça o download do programa para o seu sistema operacional.
2. Abra o Bruno no seu computador.

### Passo 2: Importar a Coleção de Testes
1. No painel inicial do Bruno, clique em **"Open Collection"** (Abrir Coleção).
2. Selecione a pasta `colecao_bruno` que está dentro desta atividade.
3. Você verá duas requisições aparecerem no painel esquerdo: 
   * `1. Obter Post Real`
   * `2. Criar Novo Post`

### Passo 3: Criar e Executar os Testes Automatizados

#### Desafio A: Testando o Contrato de Busca (`GET`)
1. Clique na requisição `1. Obter Post Real`.
2. Clique no botão de enviar (ícone de play/seta azul) para ver a resposta da API do outro lado da internet.
3. Agora vá na aba **"Assert"** (Asserções) desta requisição no Bruno.
4. Você deve configurar duas verificações automáticas:
   * **Assert 1:** Garantir que o status da resposta é igual a `200`.
     * *Configuração no Bruno:* `res.status` | `eq` | `200`
   * **Assert 2:** Garantir que o ID do autor do post (`userId`) retornado no corpo da resposta é igual a `1`.
     * *Configuração no Bruno:* `res.body.userId` | `eq` | `1`
5. Envie a requisição novamente e verifique se os testes passam (ficam verdes na aba lateral).

#### Desafio B: Testando o Contrato de Criação (`POST`)
1. Clique na requisição `2. Criar Novo Post`.
2. Vá na aba **"Body"** e veja o JSON que estamos enviando.
3. Vá na aba **"Assert"** e configure os seguintes testes:
   * **Assert 1:** O código de status de criação bem-sucedida deve ser `201`.
     * *Configuração:* `res.status` | `eq` | `201`
   * **Assert 2:** O título retornado no corpo da resposta deve ser igual ao título que enviamos no JSON original ("Aula de Testes de API").
     * *Configuração:* `res.body.title` | `eq` | `Aula de Testes de API`
4. Execute o teste e garanta que ele fique verde!

---
*Dica: Travou na sintaxe de como preencher as tabelas de Assert do Bruno? Confira a imagem explicativa na pasta `gabarito/respostas.md`.*