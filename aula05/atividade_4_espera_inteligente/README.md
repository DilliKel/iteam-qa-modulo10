# ⏳ Atividade 4: O Desafio do Tempo (Boss)

**Objetivo:** Ensinar o robô a ser paciente. 

## 📖 O Cenário
Como testar a interface é lento[cite: 16], muitas vezes o código Python tenta clicar em um botão **antes** dele aparecer na tela, estourando um `NoSuchElementException`. Você aprenderá a usar o **WebDriverWait** (Espera Explícita) para fazer o robô esperar o elemento existir.

## 🛠️ O que você deve fazer:
1. Abra `test_espera.py`.
2. Usaremos um site de testes de "atraso" que demora 5 segundos para gerar um botão.
3. Configure o `WebDriverWait` para esperar até 10 segundos pelo botão aparecer, e só então clicar nele.