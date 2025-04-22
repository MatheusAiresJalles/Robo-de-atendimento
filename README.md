

# 🤖 Robô de Atendimento Fora do Horário Comercial

Este projeto simula um robô de atendimento automatizado para responder clientes fora do horário comercial e em fins de semana, garantindo que ninguém fique sem resposta.

## 🎯 Objetivo

- Reduzir o número de clientes sem atendimento fora do expediente
- Fornecer informações úteis automaticamente
- Deixar claro que o robô **não realiza vendas**, apenas informa

## 📦 Funcionalidades

- Menu de interação com dúvidas comuns
- Registro das conversas em CSV
- Respostas automáticas com limitações claras
- Geração de gráfico comparando o atendimento **antes vs depois do robô**

## 📊 Análise de Impacto

Gráfico gerado (`comparativo_atendimento_robo.png`) mostrando a melhoria no atendimento após implementação do robô.

## 🛠️ Tecnologias Usadas

- Python
- Matplotlib
- CSV
- Terminal (input/output)

## 🚀 Como usar

1. Execute o script principal:
   ```bash
   python robo_atendimento.py

## Descrição do atendimento via robo 
Bem-vindo ao atendimento virtual!
Estamos fora do horário comercial (segunda a sexta-feira, das 8h às 18h).
Nosso robô está aqui para ajudar com dúvidas frequentes.

⚠️ *Este robô não realiza vendas ou pedidos*. Para comprar, fale com um atendente humano no horário comercial.

Escolha uma das dúvidas abaixo:
1. Queria saber o valor das canecas acrílicas
2. Vocês estão funcionando hoje?
3. Tem o catálogo das produtos disponíveis?
4. Qual o prazo de entrega para Belo Horizonte?
5. Vocês fazem canecas personalizadas?
6. Aceitam Pix como forma de pagamento?
7. Fiz um pedido pelo site e não recebi nenhuma resposta
8. Consigo agendar um pedido para semana que vem?

Digite o número da sua dúvida:
