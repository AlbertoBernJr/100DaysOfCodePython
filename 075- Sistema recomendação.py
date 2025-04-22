#Construa um sistema de recomendação

import pandas as pd
#[pandas]: Biblioteca para manipulação e análise de dados em 
# estruturas chamadas DataFrames.​

#------Dados dos filmes------
# - [filmes]: Contém o ID e o título de cada filme
filmes = pd.DataFrame({
    'filme_id': [1, 2, 3, 4, 5],
    'titulo': ['Matrix', 'Titanic', 'Vingadores', 'Toy Story', 'O Rei Leão']
})

#-----Dados das avaliações------
# - [avaliacoes]: Contém o ID do usuário, o ID do filme e a nota que 
# o usuário deu ao filme.
avaliacoes = pd.DataFrame({
    'usuario_id': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'filme_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 5],
    'nota': [5, 4, 5, 4, 5, 3, 4, 5, 4, 5]
})

#-----Calcular a média das avaliações-----
media_avaliacoes = avaliacoes.groupby('filme_id')['nota'].mean().reset_index()
media_avaliacoes.columns = ['filme_id', 'media_nota']

"""
- [ groupby('filme_id') ]: Agrupa as avaliações pelo ID do filme.
- [ ['nota'].mean() ]: Calcula a média das notas para cada grupo.
- [ reset_index() ]: Reseta o índice para transformar o resultado em
     um DataFrame.
- [ columns ]: Renomeia as colunas para 'filme_id' e 'media_nota'.​
"""
#------Juntar os dados------
filmes_com_media = pd.merge(filmes, media_avaliacoes, on='filme_id')
#[pd.merge()]:Combina os dois DataFrames com base na coluna 'filme_id'.​

#------Recomendar os filmes------
recomendacoes = filmes_com_media.sort_values(by='media_nota', ascending=False)
#[sort_values()]: Ordena o DataFrame pela coluna 'media_nota' em ordem decrescente.

#------Exibir as recomendações-----
print("Filmes recomendados:")
print(recomendacoes[['titulo', 'media_nota']])
#[['titulo', 'media_nota']]: Seleciona apenas as colunas 'titulo' e 'media_nota' para exibição.