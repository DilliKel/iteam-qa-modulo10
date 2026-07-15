# 🐉 Atividade 5: Desafio Boss - O Caos das Exceções (Nível Difícil)

**Objetivo:** Elevar o nível de isolamento. Você vai aprender a testar cenários de falha catastrófica usando múltiplos Mocks e simulando quedas de servidor.

## 📖 O Cenário
Você trabalha no e-commerce central. O código de `checkout.py` é responsável por cobrar o cartão do cliente. 

A regra de negócio é clara e possui um plano de contingência:
1. Tenta cobrar o cartão na API do Banco (Gateway).
2. Se o Banco aprovar, retorna "Pagamento Aprovado".
3. Se o Banco **cair/sair do ar** (gerando um `ConnectionError`), o sistema **NÃO pode quebrar a tela do usuário**. Ele deve capturar o erro, acionar o Mock de um sistema de alertas para **avisar o Administrador** e retornar a mensagem amigável: "Erro: Sistema indisponível no momento".

## 🛠️ O que você deve fazer:
Abra o arquivo `test_checkout.py`. Você tem duas missões difíceis usando a biblioteca `unittest.mock`:

* **Missão 1:** Mocar a API do banco e o sistema de alertas no mesmo teste. Fazer a API retornar `True` e garantir que o alerta **não** foi chamado.
* **Missão 2 (O Desafio Real):** Mocar a API do banco para **explodir um erro de conexão**. Para simular um erro em um Mock, ao invés de usar `.return_value = ...`, você precisará usar a propriedade `.side_effect = ConnectionError("Banco fora do ar")`. Depois, você deve garantir que o sistema de alertas foi acionado pedindo socorro!

---
*Dica: Respira fundo! Se a sintaxe de múltiplos Mocks bugar a mente, dê uma olhada no `GPT rsrsrs`.*