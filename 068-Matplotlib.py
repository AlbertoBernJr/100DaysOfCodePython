import matplotlib.pyplot as plt
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.ylabel("y numbers")
plt.xlabel("x numbers")

plt.show()

#gráfico barras
# Dados simulados
data = [25, 10, 15, 20]

# Criando o gráfico de barras
plt.bar(range(len(data)), data)

# Definindo os nomes das barras
plt.xticks(range(len(data)), ['A', 'B', 'C', 'D'])
plt.title('Gráfico de Barra')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Mostrando o gráfico
plt.show()
"""

#Gráfico dispersão
x = [1, 3, 5, 7, 9, 5, 4, 7, 8, 0, 3, 6, 11, 1, 2]
y = [2, 3, 7, 1, 0, 5, 7, 9, 5, 4, 7, 8, 0, 2, 3]

plt.scatter(x, y)
plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()