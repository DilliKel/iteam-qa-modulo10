# Exercícios de Fixação — Aula 01

## 1. Diferença entre QA e QC

**Quality Control (QC)** é reativo e focado no **produto**: verifica se aquilo que já foi construído (uma feature, um build, uma release) atende aos requisitos, geralmente através de testes executados sobre o artefato pronto (testes manuais, testes automatizados, homologação). É a atividade de "encontrar defeitos antes que o cliente encontre".

**Quality Assurance (QA)** é preventivo e focado no **processo**: define e melhora as práticas, padrões e fluxos de trabalho do time (revisão de código, definição de critérios de aceite, padronização de testes, CI/CD) para reduzir a probabilidade de defeitos serem introduzidos, em vez de apenas caçá-los depois.

Em resumo: QC pergunta "este produto está bom?"; QA pergunta "o nosso processo de construir produtos está bom o suficiente para gerar produtos bons consistentemente?".

## 2. E-commerce que cai com 500 acessos simultâneos

O pilar violado é principalmente a **Eficiência** (Efficiency, ISO 9126/25000) — mais especificamente o comportamento em relação ao tempo e à capacidade de uso de recursos sob carga (escalabilidade). O sistema foi validado apenas em baixa concorrência (10 usuários) e nunca teve seu comportamento sob carga real testado; ele não foi dimensionado (capacity planning) para o volume de acesso esperado em horário de pico.

Vale notar que também há uma violação de **Confiabilidade** (Reliability), já que o sistema "cai" completamente em vez de degradar graciosamente — voltando à indisponibilidade total (falha de tolerância a falhas). Mas a causa raiz do problema, nesse cenário, está em Eficiência: a aplicação nunca foi testada nem projetada para o volume real de uso.

## 3. Por que o custo de correção de um bug cresce na fase de produção

Quanto mais tarde um defeito é encontrado no ciclo de vida do software, mais caro fica corrigi-lo, por alguns motivos:

- **Quando encontrado na codificação:** o próprio desenvolvedor ainda está com o contexto do código na cabeça; a correção é imediata e isolada, sem impacto em outras partes do sistema.
- **Quando encontrado em produção:** o defeito já impactou usuários reais (perda de vendas, dados corrompidos, reputação da marca). Corrigir exige: reproduzir o problema em um ambiente diferente de onde foi escrito, identificar a causa em meio a código que já evoluiu desde então, escrever a correção, testá-la sem quebrar outras funcionalidades que já dependem do comportamento atual (efeito regressivo), aplicar um deploy emergencial (hotfix) — muitas vezes fora do fluxo normal de release — e, em alguns casos, lidar com suporte ao cliente, reembolsos ou danos à confiança na marca.

Esse fenômeno é conhecido como "curva de custo de correção" — o custo cresce de forma exponencial (não linear) a cada fase que o defeito atravessa sem ser detectado.
