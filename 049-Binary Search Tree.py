#implementar uma árvore de pesquisa binária

class No:
#Classe que representa um nó da árvore

    def __init__(self, valor):
        self.valor = valor #armazena valor do nó
        #[valor] = dado a ser guardado (ex: número, string)

        self.esquerda = None #referência ao filho esquerdo
        self.direita = None #referência ao filho direito
        #[esquerda] e [direita]: Ponteiros para os nós filhos (inicializados como None).

class ArvoreBinariaPesquisa:
#Classe que implementa uma Árvore Binária de Pesquisa
    def __init__(self): #[__init__] = método de inicialização
        self.raiz = None #a arvore começa vazia -> inicializa a ávore com o valor [none](vazia)

    def inserir(self, valor): #método para inserir
    #Insere um novo valor na árvore

        if self.raiz is None:
            self.raiz = No(valor) 
            #Se a árvore estiver vazia, cria a raiz
        else:
            self._inserir_recursivo(valor, self.raiz)
            #Caso contrário, insere recursivamente

    def _inserir_recursivo(self, valor, no_atual):
    #Método auxiliar para inserção recursiva

        if valor < no_atual.valor: #Se o valor for menor, vai para a esquerda
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)

        elif valor > no_atual.valor: #Se o valor for maior, vai para a direita
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

        # Ignora valores duplicados (não faz nada se valor == no_atual.valor)

    def buscar(self, valor):
    #Busca um valor na árvore

        return self._buscar_recursivo(valor, self.raiz) 
        #Inicia a busca pela raiz

    def _buscar_recursivo(self, valor, no_atual):
    #Método auxiliar para busca recursiva

        if no_atual is None:
            return False #Valor não encontrado
        
        if valor == no_atual.valor:
            return True #Valor encontrado
        
        elif valor < no_atual.valor:
            return self._buscar_recursivo(valor, no_atual.esquerda)
            #Busca na esquerda

        else:
            return self._buscar_recursivo(valor, no_atual.direita)
            #Busca na direita

    def remover(self, valor):
    #Remove um valor da árvore

        self.raiz = self._remover_recursivo(valor, self.raiz)
        #Inicia a remoção pela raiz

    def _remover_recursivo(self, valor, no_atual):
    #Método auxiliar para remoção recursiva

        if no_atual is None:
            return no_atual 
            #Árvore vazia ou valor não encontrado

        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_recursivo(valor, no_atual.esquerda)
            #Busca na esquerda

        elif valor > no_atual.valor:
            no_atual.direita = self._remover_recursivo(valor, no_atual.direita)
            #Busca na direita

        else:
            #Caso 1: Nó com 0 ou 1 filho
            if no_atual.esquerda is None:
                return no_atual.direita
                #Substitui pelo filho direito (ou None)

            elif no_atual.direita is None:
                return no_atual.esquerda
                #Substitui pelo filho esquerdo

            #Caso 2: Nó com 2 filhos: obtém o sucessor in-order (menor na subárvore direita)
            no_atual.valor = self._min_valor(no_atual.direita)
            #Encontra o menor valor da subárvore direita

            no_atual.direita = self._remover_recursivo(no_atual.valor, no_atual.direita)
            #Remove o sucessor

        return no_atual
        """
        Casos de Remoção:
        - Nó sem filhos: Remove diretamente.
        - Nó com 1 filho: Substitui pelo filho.
        - Nó com 2 filhos: Substitui pelo menor valor da subárvore direita (sucessor in-order).
        """

    def _min_valor(self, no):
    #Encontra o menor valor a partir de um nó
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def em_ordem(self):
    #Travessia em-ordem (esquerda, raiz, direita)

        elementos = []
        self._em_ordem_recursivo(self.raiz, elementos)
        return elementos
        # Retorna os valores em ordem crescente

    def _em_ordem_recursivo(self, no, elementos):
    #Método auxiliar para travessia em-ordem

        if no:
            self._em_ordem_recursivo(no.esquerda, elementos) #Visita esquerda
            elementos.append(no.valor) #Visita raiz
            self._em_ordem_recursivo(no.direita, elementos) #Visita direita

    def pre_ordem(self):
    #Travessia pré-ordem (raiz, esquerda, direita)
        elementos = []
        self._pre_ordem_recursivo(self.raiz, elementos)
        return elementos

    def _pre_ordem_recursivo(self, no, elementos):
    #Método auxiliar para travessia pré-ordem
        if no:
            elementos.append(no.valor)
            self._pre_ordem_recursivo(no.esquerda, elementos)
            self._pre_ordem_recursivo(no.direita, elementos)

    def pos_ordem(self):
    #Travessia pós-ordem (esquerda, direita, raiz)
        elementos = []
        self._pos_ordem_recursivo(self.raiz, elementos)
        return elementos

    def _pos_ordem_recursivo(self, no, elementos):
    #Método auxiliar para travessia pós-ordem
        if no:
            self._pos_ordem_recursivo(no.esquerda, elementos)
            self._pos_ordem_recursivo(no.direita, elementos)
            elementos.append(no.valor)
    """
    Travessias:
    - Em-ordem (esquerda → raiz → direita): Valores em ordem crescente.
    - Pré-ordem (raiz → esquerda → direita): Útil para copiar a árvore.
    - Pós-ordem (esquerda → direita → raiz): Útil para deletar a árvore.
    """

# Exemplo de uso
if __name__ == "__main__":
#- verifica se o script está sendo executado diretamente (não importado como módulo)
#- permite que o código dentro do bloco só execute quando o arquivo é rodado 
#       diretamente, mas não quando importado por outro script.

    bst = ArvoreBinariaPesquisa() #inicializa uma árvore vazia
    #[bst]= binary search tree

    valores = [50, 30, 70, 20, 40, 60, 80]
    
    for valor in valores:
        bst.inserir(valor)
    
    print("Em-ordem:", bst.em_ordem())     # [20, 30, 40, 50, 60, 70, 80]
    print("Pré-ordem:", bst.pre_ordem())   # [50, 30, 20, 40, 70, 60, 80]
    print("Pós-ordem:", bst.pos_ordem())   # [20, 40, 30, 60, 80, 70, 50]
    
    print("\nBuscar 40:", bst.buscar(40))  # True
    print("Buscar 45:", bst.buscar(45))    # False
    
    print("\nRemovendo 20...")
    bst.remover(20)
    print("Em-ordem após remoção:", bst.em_ordem())  # [30, 40, 50, 60, 70, 80]