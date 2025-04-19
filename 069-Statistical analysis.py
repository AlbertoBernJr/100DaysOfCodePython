"""
Instalando pandas -> digitar [pip install pandas] no terminal

Realizar análise estatística em um conjunto de dados
"""
#importando a biblioteca Pandas com o nome de [pd]
import pandas as pd


#--------------Carregando Dados-----------------
# Exemplo 1: Criar um DataFrame manualmente
data = {
    'Idade': [25, 30, 35, 40, 45, 50, 55, 60],
    'Salário': [3000, 4500, 5000, 6000, 8000, 7000, 9000, 8500],
    'Departamento': ['Vendas', 'TI', 'TI', 'RH', 'Vendas', 'RH', 'TI', 'Vendas']
}
df = pd.DataFrame(data)

# Exemplo 2: Carregar de um arquivo CSV
# df = pd.read_csv('dados.csv')

#---------Visualização Inicial-----------------
print("Primeiras linhas:\n", df.head())  
#Mostra as 5 primeiras linhas
print("\nInformações do DataFrame:\n", df.info())  
#Tipos de dados e valores não nulos
print("\nEstatísticas Descritivas:\n", df.describe())  
#Média, desvio padrão, quartis, etc.

#--------Medidas de Tendência Central----------
media_idade = df['Idade'].mean()
mediana_salario = df['Salário'].median()
moda_departamento = df['Departamento'].mode()[0]

print(f"\nMédia de Idade: {media_idade:.2f}")
print(f"Mediana do Salário: {mediana_salario}")
print(f"Moda do Departamento: {moda_departamento}")

#-----------Análise por Grupos-------------
# Agrupando por departamento e calculando estatísticas
grupo_departamento = df.groupby('Departamento')['Salário']
print("\nEstatísticas por Departamento:")
print(grupo_departamento.describe())

# Média salarial por departamento
print("\nMédia Salarial por Departamento:")
print(grupo_departamento.mean())