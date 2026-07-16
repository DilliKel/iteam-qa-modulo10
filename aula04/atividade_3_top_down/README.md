# 🔽 Atividade 3: Abordagem Top-Down (Nível Intermediário)

**Objetivo:** Compreender a abordagem Top-Down de integração, onde começamos pelas camadas superiores (Rotas/API) e usamos Stubs para as camadas inferiores (Banco) que ainda não estão prontas.

## 📖 O Cenário
A equipe de Backend (camada superior) terminou a rota de receber requisições HTTP da internet. Porém, a equipe de Banco de Dados (camada inferior) ainda não terminou o banco real. Como testar a rota HTTP sem o banco? 

## 🛠️ O que você deve fazer:
Abra o arquivo `test_rotas.py`. Você vai criar um **Stub** (um objeto falso muito simples, sem usar bibliotecas complexas) que finge ser o banco de dados. 
Preencha a classe `BancoStub` para que o teste de integração passe! Dúvidas? Olhe o Gabarito!