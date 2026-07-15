# Respostas — Atividades Práticas (Aula 02)

Respostas das perguntas reflexivas pedidas nos READMEs de cada atividade.

## Atividade 1 — Erro, Defeito e Falha (frete.py)

**Cenário:** regra de negócio pede frete grátis para compras "iguais ou acima" de R$ 100,00, mas o código usava `if valor_compra > 100`.

- **Erro (ação humana):** o desenvolvedor interpretou a regra "igual ou acima de R$ 100" de forma incompleta, entendendo apenas "acima de R$ 100" — esqueceu de tratar o caso de igualdade.
- **Defeito (bug no código):** [frete.py, linha 3](atividade_1_erro_defeito_falha/frete.py#L3) — o operador usado era `>` (estritamente maior) em vez de `>=` (maior ou igual).
- **Falha (comportamento visível):** ao comprar exatamente R$ 100,00, o cliente via "Frete: R$ 20,00" na tela, quando deveria ver "Frete Grátis".

**Correção aplicada:** troca de `>` por `>=` na condição.

## Atividade 2 — Código Morto (login.py)

- **Onde está o código morto:** o `print` do log de segurança estava escrito depois dos dois blocos `if`/`else`, que já continham `return` em ambos os ramos ([login.py](atividade_2_codigo_morto/login.py)).
- **Por que nunca era executado:** a instrução `return` encerra a execução da função imediatamente. Como os dois únicos caminhos possíveis (`idade >= 18` e `idade < 18`) terminavam em `return`, não existia nenhum fluxo de execução que chegasse até o `print` — ele estava estruturalmente inalcançável, independente do valor de `idade` testado.

**Correção aplicada:** o `print` do log foi movido para antes de cada `return`, garantindo que o registro de auditoria seja impresso sempre, antes da função devolver a resposta.

## Atividade 4 — Regressão (sistema_pix.py)

- **Bug introduzido:** ao adicionar a nova regra de limite diário, o desenvolvedor reescreveu a validação antiga `valor_transferencia <= 0` como `valor_transferencia < 0` ([sistema_pix.py, linha 7](atividade_4_teste_de_regressao/sistema_pix.py#L7)). Isso passou a permitir transferências de R$ 0,00, que antes eram corretamente rejeitadas.
- **Por que testes automatizados são cruciais ao alterar código antigo:** sem a bateria de testes de regressão, essa mudança silenciosa (aceitar Pix de R$ 0,00) teria ido para produção sem ninguém perceber — a nova feature "funcionava", mas uma regra antiga válida foi quebrada como efeito colateral. Testes automatizados rodam toda a bateria antiga a cada alteração, expondo esse tipo de quebra imediatamente, antes que o código chegue ao usuário final.

**Correção aplicada:** validação revertida para `<= 0`, mantendo a nova regra de limite diário intacta.
