#Implemente um algoritmo de busca em profundidade (DFS)

def dfs(grafo, nodo, visitados=None):
    """
    Função que realiza a busca em profundidade (DFS) em um grafo.
    
    Parâmetros:
      - grafo: Um dicionário onde cada chave é um nó e o valor é uma lista 
               de nós adjacentes (vizinhos).
      - nodo: O nó atual que está sendo visitado.
      - visitados: Um conjunto que armazena os nós que já foram visitados 
                   para evitar visitas repetidas. Se não for informado, 
                   será criado um conjunto vazio.
    
    Retorna:
      - O conjunto com todos os nós visitados a partir do nó inicial.
    """
    
    # Se o conjunto de visitados ainda não foi criado, inicia um conjunto vazio.
    if visitados is None:
        visitados = set()  
        # Conjunto para guardar os nós visitados.
    
    # Adiciona o nó atual ao conjunto de visitados.
    visitados.add(nodo)
    
    # Imprime o nó atual para acompanhar a ordem da visita.
    print(nodo)
    
    """
    Para cada vizinho do nó atual, obtido a partir do grafo.
    A função grafo.get(nodo, []) retorna a lista de vizinhos se o nó existir
        ou uma lista vazia no caso dele não ter vizinhos (evitando erros).
    """
    for vizinho in grafo.get(nodo, []):
        # Se o vizinho ainda não foi visitado, chamamos a função recursivamente.
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)
    
    # Após visitar todos os nós conectados, retorna o conjunto de visitados.
    return visitados


# Exemplo de uso do algoritmo DFS
if __name__ == "__main__":
    # Define um grafo como um dicionário:
    # Cada chave representa um nó e o valor associado é uma lista de nós vizinhos.
    grafo_exemplo = {
        'A': ['B', 'C'],   # O nó 'A' está conectado aos nós 'B' e 'C'.
        'B': ['D', 'E'],   # O nó 'B' está conectado aos nós 'D' e 'E'.
        'C': ['F'],        # O nó 'C' está conectado ao nó 'F'.
        'D': ['G'],        # O nó 'D' está conectado ao nó 'G'.
        'E': [],           # O nó 'E' não possui conexões.
        'F': [],           # O nó 'F' não possui conexões.
        'G': []            # O nó 'G' não possui conexões.
    }
    
    print("Ordem de visitação (DFS):")
    # Inicia a busca em profundidade a partir do nó 'A'.
    dfs(grafo_exemplo, 'A')
