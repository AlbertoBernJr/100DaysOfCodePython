#implementar uma estrutura de dados de pilha
"""
Uma pilha é uma coleção de elementos que segue o princípio LIFO 
(Last In, First Out), ou seja, o último elemento a ser inserido é 
o primeiro a ser removido.
"""

class Pilha:
    def __init__(self):
        #Inicializa uma pilha vazia
        self.__elementos = [] #Lista para armazenar os elementos da pilha

    def esta_vazia(self):
        """
        - verifica se a pilha esta vazia
        - retorna [true] se a pilha estiver vazia
        - retorna [False] se a pilha não estiver vazia
        """
        return len(self.__elementos) == 0
        #[len()]=retorna a quantidade de valores que estão dentro da lista

    def empilhar(self, elemento):
        """
        Adiciona um elemento ao topo da pilha [elementos]usando o método 
        [append()]
        """
        self.__elementos.append(elemento)

    def desempilhar(self):
        """
        Remove e retorna o elemento do topo da pilha usando o método
        [pop()]
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia. Não é possível desempilhar.")
            #se a pilha estiver vazia, ativa a exceção [IndexError]

        return self.__elementos.pop()
        #retorna o valor que foi desempilhado

    def topo(self):
    #Retorna o elemento no topo da pilha sem removê-lo

        if self.esta_vazia():
            raise IndexError("A pilha está vazia. Não há elemento no topo.")
        
        return self.__elementos[-1]
        #retorna o elemento que esta no topo

    def tamanho(self):
    #Retorna o número de elementos na pilha usando a função [len()]

        return len(self.__elementos)
        #retorna a quantidade de elementos

    def __str__(self):
        #Retorna uma representação em string da pilha -> mostra todos os elementos
        return str(self.__elementos)
    
#----------------------------------------------------------------------------
# Criando uma pilha
pilha = Pilha()

# Empilhando elementos
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)

# Exibindo a pilha
print("Pilha:", pilha)

# Acessando o topo da pilha
print("Topo da pilha:", pilha.topo())

# Desempilhando elementos
print("Desempilhado:", pilha.desempilhar())
print("Pilha após desempilhar:", pilha)  

# Verificando o tamanho da pilha
print("Tamanho da pilha:", pilha.tamanho())

# Verificando se a pilha está vazia
print("A pilha está vazia?", pilha.esta_vazia())

# Desempilhando todos os elementos
pilha.desempilhar()
pilha.desempilhar()

# Tentando desempilhar de uma pilha vazia
try:
    pilha.desempilhar()
except IndexError as e:
    print(e)  # Saída: A pilha está vazia. Não é possível desempilhar.