#carregar e manipular dados usando Pandas

#Importar o Pandas e 
import pandas as pd

# Criar Dados fictícios de vendas
dados = {
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Quantidade': [5, 10, 8, 3],
    'Preço_Unitário': [3500, 150, 300, 1200]
}

# Criar DataFrame
df = pd.DataFrame(dados)
print("DataFrame Original:")
print(df)

#Adicionar uma coluna de "Total" (Quantidade × Preço)
df['Total'] = df['Quantidade'] * df['Preço_Unitário']
print("\nDataFrame com Total:")
print(df)

#Filtrar produtos com vendas acima de R$ 2000
vendas_altas = df[df['Total'] > 2000]
print("\nProdutos com Total > 2000:")
print(vendas_altas)