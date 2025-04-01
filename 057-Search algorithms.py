#Implementar algoritmos de busca (por exemplo, busca binária)

def busca_binaria(lista, alvo):
    """
    Função que realiza a busca binária em uma lista ordenada.
    
    Parâmetros:
      - lista: Uma lista de elementos já ordenados (do menor para o maior).
      - alvo: O elemento que desejamos encontrar.
      
    Retorna:
      - [O] índice do elemento encontrado na lista;
      - [-1], caso o elemento não seja encontrado.
    """
    inicio = 0                 
    # Inicia a variável 'inicio' na posição 0 (primeiro elemento da lista).
    fim = len(lista) - 1       
    # 'fim' recebe o último índice da lista, obtido pelo tamanho da lista menos um.
    
    # O loop continua enquanto o intervalo (entre 'inicio' e 'fim') for válido.
    while inicio <= fim:
        meio = (inicio + fim) // 2  
        #Calcula o índice do meio: soma 'inicio' com 'fim',
        #   e divide por 2 (divisão inteira) para pegar o meio.
        
        if lista[meio] == alvo:     
        # Compara o elemento no índice 'meio' com o 'alvo';
            return meio             
            # Se forem iguais, o elemento foi encontrado e retorna o índice.
        
        elif lista[meio] < alvo:
            #Se o elemento do meio é menor que o 'alvo', 
            #   descartamos a metade esquerda, pois apenas a parte direita pode conter o elemento.
            inicio = meio + 1      
            # Move o 'inicio' para a posição imediatamente após 'meio'.
        
        else:
        #Se o elemento do meio é maior que o 'alvo',
        #   descartamos a metade direita, pois apenas a parte esquerda pode conter o elemento.
            fim = meio - 1         
            #Move o 'fim' para a posição imediatamente anterior a 'meio'.
    
    return -1                      
    #Se todo o intervalo for examinado sem encontrar o 'alvo',
    #   retorna -1 para indicar que o elemento não está presente na lista.

#Exemplo de uso da função:

#Criamos uma lista já ordenada. Lembre-se: a busca binária só funciona 
#   corretamente com listas ordenadas.
lista_exemplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
valor_pesquisado = 7            
# Definimos o valor que queremos encontrar na lista.
resultado = busca_binaria(lista_exemplo, valor_pesquisado)

#Verificamos se a função retornou um índice válido (ou seja, diferente 
#   de -1).
if resultado != -1:
    print("Elemento", valor_pesquisado, "encontrado no índice", resultado)
else:
    print("Elemento", valor_pesquisado, "não encontrado.")