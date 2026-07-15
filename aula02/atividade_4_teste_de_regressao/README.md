# 🔄 Atividade 4: O Fantasma da Regressão (Nível Intermediário)

**Objetivo:** Compreender na prática a importância do **Teste de Regressão**. Você precisará identificar um defeito inserido acidentalmente em um código que já estava funcionando, após a adição de uma nova regra de negócio.

## 📖 O Cenário
O aplicativo bancário da Atividade 3 foi um sucesso! Agora, o banco pediu uma atualização (uma nova *feature*):
> *"Por questões de segurança, a transferência Pix agora precisa respeitar um **Limite Diário** estabelecido pelo usuário."*

O desenvolvedor pegou o código antigo, adicionou a nova regra do limite diário e entregou o sistema. No entanto, ao rodarmos os nossos "Testes Antigos" (Testes de Regressão), percebemos que **uma das regras originais parou de funcionar**!

## 🛠️ O que você deve fazer:
1. Abra o arquivo `sistema_pix.py`.
2. Rode o código e observe a saída da "Bateria de Testes de Regressão" no terminal.
3. Compare o que foi impresso no terminal com o comentário `Esperado:` ao lado de cada teste. Algum deles falhou?
4. Responda: 
   * Qual foi o bug (defeito) que o desenvolvedor introduziu acidentalmente ao tentar colocar a nova regra do Limite Diário?
   * Por que é crucial ter testes automatizados rodando sempre que mexemos em um código antigo?
5. **Corrija o código** para que a nova regra funcione **sem quebrar** as regras antigas. Todos os testes devem passar!

---
*Dica: Após resolver, confira a pasta `gabarito/respostas.md`.*