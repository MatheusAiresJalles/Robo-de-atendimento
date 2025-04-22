import matplotlib.pyplot as plt

# Dados simulados com mais detalhes
problemas = [
    "Consulta de preços", 
    "Solicitação de catálogo", 
    "Pergunta sobre horário", 
    "Dúvida sobre entrega", 
    "Pedido de personalização", 
    "Outros"
]

# Antes do robô: atendimentos realizados manualmente (simulados)
antes_do_robo = [5, 3, 2, 4, 1, 0]

# Depois do robô: atendimentos realizados automaticamente
depois_do_robo = [30, 25, 15, 20, 10, 5]

# Cores para o gráfico
cores = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Criar o gráfico de barras comparativo
plt.figure(figsize=(12, 6))
bar_width = 0.35
index = range(len(problemas))

plt.bar(index, antes_do_robo, bar_width, color='red', label='Antes do Robô')
plt.bar([i + bar_width for i in index], depois_do_robo, bar_width, color=cores, label='Depois do Robô')

plt.xlabel('Tipo de Problema')
plt.ylabel('Atendimentos Realizados')
plt.title('Comparativo de Atendimentos Fora do Horário Comercial')
plt.xticks([i + bar_width / 2 for i in index], problemas, rotation=30)
plt.legend()
plt.tight_layout()

# Exibir o gráfico
plt.show()
