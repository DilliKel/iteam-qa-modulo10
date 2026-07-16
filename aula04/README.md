# 🧪 Aula 04: Integração, Regressão e Validação do Sistema

Bem-vindos(as) à nossa quarta missão prática! 🚀

Na aula anterior, aprendemos a isolar nosso código usando Mocks e Stubs. Mas o que acontece quando precisamos que as peças do quebra-cabeça funcionem **juntas**? 

Hoje, vamos subir um degrau na Pirâmide de Testes e trabalhar com **Testes de Integração** e **Testes de Regressão**. O nosso objetivo é garantir que a comunicação entre o banco de dados e as regras de negócio ocorra sem ruídos, e que novas alterações no código não quebrem o que já estava funcionando!

## 🗺️ As Missões de Hoje:

1. **[Atividade 1: A Integração Real](./atividade_1_integracao_real):** Sem Mocks! Vamos colocar o Serviço de Pedidos para conversar de verdade com um Banco de Dados Fictício.
2. **[Atividade 2: O Bug de Regressão](./atividade_2_bug_de_regressao):** Você fará uma alteração inofensiva no código e verá como a nossa suíte de testes salva o sistema de um desastre em produção.
3. **[Atividade 3: Abordagem Top-Down (Intermediário)](./atividade_3_top_down):** Como testar a camada visual (API) quando o banco de dados ainda não está pronto? Vamos usar Stubs!
4. **[Atividade 4: Visão Ponta-a-Ponta (Boss)](./atividade_4_ponta_a_ponta):** O teste definitivo. Simularemos o fluxo completo: da interface do usuário até a gravação no banco de dados.

## 🚀 Preparação
Abra o terminal na raiz deste projeto e certifique-se de que o pytest está instalado:
`pip install pytest`

Vamos codar! 💻🔍