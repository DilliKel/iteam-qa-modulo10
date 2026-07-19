# Exercícios de Fixação — Aula 05 (Dia 5)

## 1. Falso Positivo / Falso Negativo na automação, e a relação com manutenção de scripts

Um **Falso Positivo** é quando o teste automatizado **falha**, mas o sistema na verdade está funcionando corretamente — o problema está no próprio script de teste (um seletor desatualizado, um tempo de espera insuficiente), não no código de produção. Um **Falso Negativo** é o oposto e mais perigoso: o teste **passa** (fica verde), mas existe um defeito real no sistema que o teste simplesmente não conseguiu detectar — por exemplo, um assert fraco demais que não checa o dado certo.

Isso se conecta diretamente com a necessidade de manutenção constante dos scripts: vivemos esse exato problema na prática nas [Atividades 1 a 4 da Aula 05](README.md). O teste da Atividade 2 (busca na Wikipédia) começou dando um Falso Positivo de reprovação — o `ElementNotInteractableException` não significava que a busca da Wikipédia estava quebrada, significava que o **nosso script** não tinha considerado que a janela do navegador abre pequena e esconde a barra de busca no layout responsivo. Se não tivéssemos investigado a causa raiz e corrigido o teste (`maximize_window()` + espera explícita), o script continuaria "mentindo" sobre o estado real do sistema — e é exatamente esse tipo de manutenção constante (a interface muda, o layout muda, o timing muda) que torna testes de UI mais caros de manter do que testes de unidade.

## 2. Por que testes de API são mais rápidos e estáveis que testes de UI

Um teste de API se comunica diretamente com o backend via requisição HTTP, sem precisar renderizar HTML, aplicar CSS, executar JavaScript client-side ou aguardar o navegador desenhar a tela — ele valida só o contrato de dados (status code, formato do payload), então não depende de elementos visuais existirem, estarem visíveis ou carregados.

Vivemos essa diferença de estabilidade na prática: os testes de API da [Atividade 5 e 6 da Aula 04](../aula04/atividade_5_testes_api_bruno/) rodam em milissegundos e nunca falharam por motivo de timing. Já os testes de UI da Aula 05 exigiram tratamento explícito pra dois problemas causados unicamente pela camada visual — um elemento escondido por causa do tamanho da janela, e uma corrida entre o código e o carregamento real da página no navegador. Numa arquitetura Full Stack separada (Front-end consumindo API de forma independente), testar a API isoladamente elimina toda essa fragilidade — você garante que o contrato de dados está correto sem pagar o custo de renderização, e sobra pro teste de UI validar só a experiência visual em si, não a lógica de negócio.

## 3. Etapas de um pipeline de CI/CD, do `git push` até a Produção

```
Desenvolvedor            Servidor de CI/CD                          Produção
     │                         │                                        │
     │  1. git push            │                                        │
     ├────────────────────────▶│                                        │
     │                         │  2. Baixa o código e as dependências   │
     │                         │  3. Roda os testes automatizados:      │
     │                         │     • Testes de Unidade (Aula 03)      │
     │                         │     • Testes de Integração (Aula 04)   │
     │                         │     • Testes de API (Aula 04)          │
     │                         │     • Testes de UI (Aula 05)           │
     │                         │                                        │
     │                         │  4. Algum teste falhou?                │
     │                         │     ├─ SIM → build rejeitado,          │
     │                         │     │        deploy bloqueado,         │
     │                         │     │        dev é avisado             │
     │                         │     └─ NÃO → build aprovado            │
     │                         │  5. Gera o artefato/imagem da aplicação│
     │                         ├───────────────────────────────────────▶│
     │                         │                       6. Deploy em Produção
```

Os testes automatizados são disparados logo depois do código ser baixado no servidor de CI (passo 3), **antes** de qualquer artefato ser gerado ou publicado. Esse é o ponto crítico do pipeline: se qualquer teste falhar (seja de unidade, integração, API ou UI), o processo é interrompido ali mesmo — o build é rejeitado e o deploy para produção é bloqueado imediatamente, garantindo que só código validado pela suíte inteira chegue ao usuário final.
