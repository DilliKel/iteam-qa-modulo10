# 🌍 Atividade Prática: Testando Integração de API com ViaCEP

**Objetivo:** Usar a ferramenta Bruno (usebruno.com) para fazer requisições HTTP reais (GET) para uma API pública (ViaCEP) e criar testes automatizados que validam a estrutura dos dados recebidos.

## 📖 O Cenário
O nosso e-commerce precisa calcular o frete das entregas. Para isso, integramos o nosso sistema com a API pública dos Correios/ViaCEP. 

O nosso contrato de integração exige que:
1. Se enviarmos um CEP válido, a API deve retornar `Status 200 OK` e um JSON contendo os dados da cidade (ex: São Paulo).
2. Se enviarmos um CEP que não existe (mas com formato válido), a API tem um comportamento peculiar: ela também retorna `Status 200 OK`, mas envia um JSON contendo a propriedade `"erro": true`. Nós precisamos testar isso!

---

## 🛠️ O que você deve fazer:

### Passo 1: Preparando o Bruno
1. Abra o programa **Bruno**.
2. Clique em **"Open Collection"** e selecione a pasta `colecao_viacep` que está dentro desta atividade.

### Passo 2: Testando o Caminho Feliz (CEP Válido)
1. Abra a requisição `1. Consultar CEP Valido`.
2. Observe que a URL está apontando para `https://viacep.com.br/ws/01001000/json/` (CEP da Praça da Sé, SP).
3. Clique em enviar (Play) e olhe a aba **Response** para ver o JSON real voltando da internet.
4. Vá na aba **"Assert"** e crie as seguintes regras de teste:
   * Valide se o status da resposta é 200.
   * Valide se a propriedade `localidade` (cidade) retornou o valor `São Paulo`.
   * Valide se a propriedade `uf` (estado) retornou `SP`.
5. Rode a requisição novamente e veja todos os testes ficarem verdes!

### Passo 3: Testando o Caminho Triste (CEP Inexistente)
1. Abra a requisição `2. Consultar CEP Inexistente`.
2. A URL aponta para `https://viacep.com.br/ws/99999999/json/` (Um CEP que não existe).
3. Envie a requisição e observe a resposta.
4. Vá na aba **"Assert"** e crie testes para garantir que:
   * O status da resposta seja 200 (Sim, o ViaCEP retorna 200 mesmo sem achar a rua!).
   * A propriedade `erro` venha com o valor booleano `true`.

---

## 💻 Alternativa: rodando pelo terminal (Bruno CLI)

Se não quiser instalar o app gráfico, o Bruno também tem uma versão de linha de comando que roda os mesmos arquivos `.bru` da pasta `colecao_viacep/`, incluindo as asserções da aba "Assert".

**Instalação (uma vez só, requer Node.js):**

```bash
npm install -g @usebruno/cli
```

**Execução:**

```bash
cd aula04/atividade_6_consulta_cep_bruno/colecao_viacep
bru run
```

A saída mostra cada requisição, cada asserção (✓ ou ✕) e um resumo final com o total de requisições/asserções que passaram — o mesmo resultado que você veria na interface gráfica, só que direto no terminal.

> **Atenção ao testar o CEP inexistente:** a API do ViaCEP devolve a propriedade `erro` como a **string** `"true"`, não como o booleano `true`. Por isso o assert do arquivo `2. Consultar CEP Inexistente.bru` está configurado como `res.body.erro: eq "true"` (com aspas).

Há também uma versão equivalente escrita em `pytest` (arquivo [`test_api_cep.py`](test_api_cep.py)), caso prefira validar via Python em vez do formato `.bru`:

```bash
python -m pip install requests
python -m pytest -v
```

---
*Dica: Não sabe como escrever a regra na aba Assert? Olhe a pasta `gabarito`!*