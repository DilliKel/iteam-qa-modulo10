# 🚀 Atividade 4: Visão Ponta-a-Ponta (Boss)

**Objetivo:** Criar um teste E2E (End-to-End) que atravessa todas as camadas do sistema. Aqui, **Mocks são proibidos**. O banco tem que ser real e os serviços secundários também.

## 📖 O Cenário
Você vai testar o fluxo de "Cadastro de Produto". O fluxo é:
1. O usuário digita os dados na Interface.
2. A Interface manda para o Controlador.
3. O Controlador manda para o Banco de Dados.

## 🛠️ O que você deve fazer:
Abra o arquivo `test_e2e.py`. Instancie todas as peças reais do arquivo `fluxo.py`, encaixe-as como um quebra-cabeça (passando uma dependência para dentro da outra) e valide se o dado digitado na Interface chegou até a variável interna do Banco de Dados!