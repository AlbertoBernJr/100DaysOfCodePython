#implementar uma estrutura de dados de fila

"""
Uma fila é uma coleção de elementos que segue o princípio FIFO 
(First In, First Out), ou seja, o primeiro elemento a ser inserido 
é o primeiro a ser removido.
"""

class Fila:
    def __init__(self):
    #Inicializa uma fila vazia
        self.__elementos = []  
        # Lista para armazenar os elementos da fila
        #Inicializa a fila com uma lista vazia [self.__elementos]

    def esta_vazia(self):
    #Verifica se a fila está vazia
        return len(self.__elementos) == 0
        #retorna [True] se a lista estiver vazia
        #retorna [False] se a lista não estiver vazia

    def enfileirar(self, elemento):
    #Adiciona um elemento ao final da fila usando [.append()]
        self.__elementos.append(elemento)

    def desenfileirar(self):
    #Remove e retorna o elemento no início da fila usando [ .pop(0)]

        if self.esta_vazia():
            raise IndexError("A fila está vazia. Não é possível desenfileirar.")
            #se a lista estiver vazia, ativa a exceção [ IndexError ]

        return self.__elementos.pop(0)
        #retorna o elemento que foi removido

    def frente(self):
    #Retorna o elemento no início da fila sem removê-lo

        if self.esta_vazia():
            raise IndexError("A fila está vazia. Não há elemento na frente.")
        
        return self.__elementos[0]
        #retorna o valor que esta no inicio da fila

    def tamanho(self):
    #Retorna o número de elementos na fila usando [len()]
        return len(self.__elementos)

    def __str__(self):
    #Retorna uma representação em string da fila usando [ __str__]

        return str(self.__elementos)
        #exibe os elementos

#----------------------------------------------------------
# Criando uma fila
fila = Fila()

# Enfileirando elementos
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)

# Exibindo a fila
print("Fila:", fila) 

# Acessando o elemento na frente da fila
print("Frente da fila:", fila.frente())

# Desenfileirando elementos
print("Desenfileirado:", fila.desenfileirar())
print("Fila após desenfileirar:", fila)

# Verificando o tamanho da fila
print("Tamanho da fila:", fila.tamanho())

# Verificando se a fila está vazia
print("A fila está vazia?", fila.esta_vazia())

# Desenfileirando todos os elementos
print("Desenfileirando o valor: ", fila.frente())
fila.desenfileirar()

print("Desenfileirando o valor: ", fila.frente())
fila.desenfileirar()

# Tentando desenfileirar de uma fila vazia
try:
    fila.desenfileirar()
except IndexError as e:
    print(e)  # Saída: A fila está vazia. Não é possível desenfileirar.