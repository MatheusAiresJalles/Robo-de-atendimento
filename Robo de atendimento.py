import random
import csv
from datetime import datetime

# =======================
# SIMULAÇÃO DE ATENDIMENTO
# =======================
def simular_atendimento():
    print("Bem-vindo ao atendimento virtual!")
    print("Estamos fora do horário comercial (segunda a sexta-feira, das 8h às 18h).")
    print("Nosso robô está aqui para ajudar com dúvidas frequentes.\n")
    print("⚠️ *Este robô não realiza vendas ou pedidos*. Para comprar, fale com um atendente humano no horário comercial.\n")

    mensagens_recebidas = [
        "Queria saber o valor das canecas acrílicas",
        "Vocês estão funcionando hoje?",
        "Tem o catálogo das produtos disponíveis?",
        "Qual o prazo de entrega para Belo Horizonte?",
        "Vocês fazem canecas personalizadas?",
        "Aceitam Pix como forma de pagamento?",
        "Fiz um pedido pelo site e não recebi nenhuma resposta",
        "Consigo agendar um pedido para semana que vem?"
    ]

    respostas = {
        "Queria saber o valor das canecas acrílicas": "As canecas acrílicas custam R$ 3,10 por unidade. Temos também modelos gel por R$ 5,00 a unidade.",
        "Vocês estão funcionando hoje?": "Agora estamos fora do horário comercial. Nosso atendimento é de segunda a sexta, das 8h às 18h.",
        "Tem o catálogo das produtos disponíveis?": "Claro! Aqui está o link para o nosso catálogo digital: [link_catalogo]",
        "Qual o prazo de entrega para Belo Horizonte?": "O prazo médio para BH é de 5 a 7 dias úteis após a confirmação do pedido.",
        "Vocês fazem copos personalizadas?": "Sim! Fazemos personalização com o nome ou arte do cliente. O atendimento humano envia o mockup no horário comercial.",
        "Aceitam Pix como forma de pagamento?": "Sim, aceitamos Pix, transferência bancária e cartões de débito ou crédito via link de pagamento.",
        "Fiz um pedido pelo site e não recebi nenhuma resposta": "Pedimos desculpas! Seu pedido será verificado por um atendente humano no próximo dia útil conforme descrição no site.",
        "Consigo agendar um pedido para semana que vem?": "O agendamento precisa ser feito com um atendente humano. Envie sua solicitação no horário comercial e cuidaremos disso para você."
    }

    print("Escolha uma das dúvidas abaixo:")
    for i, msg in enumerate(mensagens_recebidas, start=1):
        print(f"{i}. {msg}")

    try:
        opcao = int(input("\nDigite o número da sua dúvida: ")) - 1

        if 0 <= opcao < len(mensagens_recebidas):
            msg = mensagens_recebidas[opcao]
            resposta = respostas.get(msg, "Desculpe, não consegui entender. Um atendente humano irá te ajudar assim que possível.")
            print(f"\nCliente: {msg}")
            print(f"Robô: {resposta}\n")

            with open("log_conversas_robo.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([datetime.now(), "Cliente", msg, resposta])
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite o número correspondente à sua dúvida.")

# =======================
# MENU PRINCIPAL
# =======================
def menu():
    while True:
        print("\n== MENU DO ROBÔ DE ATENDIMENTO ==")
        print("1. Rodar robô (simular atendimento)")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            simular_atendimento()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar menu
if __name__ == "__main__":
    menu()
