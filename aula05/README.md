# 🤖 Aula 05: Automação de Interface (UI) com Selenium

Bem-vindos(as) ao laboratório de Automação Visual! 

Hoje vamos sair dos bastidores (APIs e Bancos de Dados) e vir para o palco: a tela do usuário! 
Como vimos na teoria, testar a interface é um processo mais lento, mas é o teste que mais se aproxima do comportamento real de um ser humano usando o sistema.

Nossa ferramenta de trabalho será o **Selenium**, o pioneiro e mais robusto framework de automação do mercado, excelente para testar sistemas complexos diretamente no navegador[cite: 16].

## 🗺️ As Missões de Hoje:

1. **[Atividade 1: O Primeiro Robô](./atividade_1_primeiros_passos):** Fazer o Selenium abrir o navegador sozinho e ler o título de um site.
2. **[Atividade 2: Interagindo com a Tela](./atividade_2_interacao):** Ensinar o robô a digitar em um campo de busca e apertar Enter.
3. **[Atividade 3: Preenchendo Formulários](./atividade_3_formularios):** Fazer login em um e-commerce de testes automatizado.
4. **[Atividade 4: O Desafio do Tempo (Boss)](./atividade_4_espera_inteligente):** O robô é mais rápido que a internet! Aprender a fazer o robô esperar a tela carregar antes de clicar.

## 🛠️ Preparação
No terminal, instale o `pytest` e o `selenium`:
`pip install pytest selenium`

*(Nota: O Selenium moderno já baixa o driver do Chrome/Edge automaticamente!)*