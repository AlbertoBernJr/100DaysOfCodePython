"""
implementar uma estrutura de dados de grafo

estrutura de dados de grafo é uma forma de representar um conjunto de objetos 
    (chamados de vértices ou nós) e as conexões entre eles (chamadas de arestas). 
    Essa estrutura é fundamental para modelar relações complexas e interconexões 
    em diversos domínios, como redes sociais, sistemas de transporte e circuitos 
    eletrônicos.

Elementos de um Grafo:
- Vértices (Nodos): Entidades individuais dentro do grafo.
- Arestas: Conexões entre os vértices, que podem ser direcionadas (com sentido) ou 
    não direcionadas (sem sentido).

Aplicações de Grafos:
Grafos são utilizados para modelar e resolver problemas em diversas áreas, como:
- Redes Sociais: Representando usuários como vértices e amizades como arestas.
- Sistemas de Transporte: Modelando cidades como vértices e rotas como arestas.
- Circuitos Eletrônicos: Onde componentes são vértices e conexões elétricas são 
    arestas.
"""

from collections import deque
#[deque]: Usado para a busca em largura (BFS) por ser eficiente em 
#   operações de fila

class Grafo:
    def __init__(self, direcionado=False):
    #Inicializa o grafo.
    #parametro [direcionado]: Se [True], o grafo é direcionado (arestas 
    # têm direção).

        self._grafo = {}
        """
        Dicionário para armazenar:
        - Chaves: Vértices (ex: "A", "B").
        - Valores: Dicionários de vizinhos e pesos (ex: {"B": 5, "C": 3}).
        """
        self._direcionado = direcionado
        #Se [False], o grafo é não direcionado (arestas são bidirecionais).

    def adicionar_vertice(self, vertice):
        """
        - Adiciona um vértice ao grafo se ele não existir
        - verifica se o vértice ja existe antes de adicionar
        """
        if vertice not in self._grafo:
            self._grafo[vertice] = {}
            #Inicializa um vértice sem vizinhos

    def adicionar_aresta(self, origem, destino, peso=1):
        """
        Adiciona uma aresta entre dois vértices.
        parametro [origem]: Vértice de origem.
        parametro [destino]: Vértice de destino.
        parametro [peso]: Peso da aresta (opcional, padrão=1).
        """
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        self._grafo[origem][destino] = peso
        #Adiciona a aresta origem → destino com um peso

        if not self._direcionado:
            self._grafo[destino][origem] = peso  # Aresta bidirecional
            #Se o grafo for não direcionado, também adiciona destino → origem

    def remover_vertice(self, vertice):
    #Remove um vértice e todas as arestas conectadas a ele

        if vertice in self._grafo:
        #Remove referências ao vértice em outros nós

            for v in self._grafo:
                if vertice in self._grafo[v]:
                    del self._grafo[v][vertice]
            
            del self._grafo[vertice]# Remove o vértice

    def remover_aresta(self, origem, destino):
    #Remove uma aresta entre dois vértices
    #Remove a aresta origem → destino (e destino → origem se for não direcionado).

        if origem in self._grafo and destino in self._grafo[origem]:
            del self._grafo[origem][destino]
            if not self._direcionado:
                del self._grafo[destino][origem] #Remove a bidirecional

    def vertices(self):
    #Retorna a lista de vértices do grafo
        return list(self._grafo.keys())

    def arestas(self):
    #Retorna a lista de arestas do grafo no formato (origem, destino, peso)

        arestas = []
        for origem in self._grafo:
            for destino, peso in self._grafo[origem].items():
                arestas.append((origem, destino, peso))
                #Tuplas (origem, destino, peso)

        return arestas

    def vizinhos(self, vertice):
    #Retorna os vértices conectados ao vértice especificado
        return list(self._grafo[vertice].keys()) if vertice in self._grafo else []

    def busca_em_largura(self, inicio):
    #Realiza uma busca em largura (BFS) a partir de um vértice

        visitados = set()
        fila = deque([inicio]) #Usa deque para eficiência
        ordem_visita = []

        while fila:
            vertice = fila.popleft() #Remove o primeiro da fila
            if vertice not in visitados:
                visitados.add(vertice)
                ordem_visita.append(vertice)
                for vizinho in self.vizinhos(vertice):
                    if vizinho not in visitados:
                        fila.append(vizinho) #Adiciona vizinhos não visitados

        return ordem_visita
        #Explora todos os vizinhos de um vértice antes de avançar (nível por nível)

    def busca_em_profundidade(self, inicio):
    #Realiza uma busca em profundidade (DFS) a partir de um vértice
    #Explora o máximo possível em um ramo antes de retroceder

        visitados = set()
        pilha = [inicio] #Usa uma pilha
        ordem_visita = []

        while pilha:
            vertice = pilha.pop() #Remove o último adicionado
            if vertice not in visitados:
                visitados.add(vertice)
                ordem_visita.append(vertice)
                for vizinho in reversed(self.vizinhos(vertice)):  
                # Ordem inversa para correta DFS

                    if vizinho not in visitados:
                        pilha.append(vizinho)
        return ordem_visita
    
    def __str__(self):
    #Representação em string do grafo
        return "\n".join(
            f"{origem} -> {', '.join(f'{destino}({peso})' for destino, peso in destinos.items())}"
            for origem, destinos in self._grafo.items()
        )

# ---------------------------Exemplo de uso------------------------------
if __name__ == "__main__":
#Cria um grafo NÃO direcionado

    grafo = Grafo(direcionado=False)
    grafo.adicionar_aresta("A", "B", 5)
    grafo.adicionar_aresta("A", "C", 3)
    grafo.adicionar_aresta("B", "D", 2)
    grafo.adicionar_aresta("C", "D", 1)

    print("Grafo:")
    print(grafo) #Mostra a estrutura

    print("\nVértices:", grafo.vertices()) #['A', 'B', 'C', 'D']
    print("Arestas:", grafo.arestas()) #[('A', 'B', 5), ('A', 'C', 3), ...]

    print("Vizinhos de 'A':", grafo.vizinhos("A"))

    print("\nBusca em Largura (BFS) a partir de 'A':", grafo.busca_em_largura("A"))
    #['A', 'B', 'C', 'D']

    print("Busca em Profundidade (DFS) a partir de 'A':", grafo.busca_em_profundidade("A"))
    #['A', 'C', 'D', 'B']

    # Remove uma aresta e um vértice
    grafo.remover_aresta("A", "C")
    grafo.remover_vertice("D")

    print("\nGrafo após remoções:")
    print(grafo) #A -> B(5); B -> A(5); C ->