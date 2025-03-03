# Write a function to count the frequency of words in a sentence

def contar_frequencia_palavras(frase):
    
    frase=frase.strip('.,!?').lower()
    # Remover pontuações e converter para minúsculas para evitar duplicações
    #remove the pontuations and convert to lower case to prevent duplication
    # separate the words and add in a list
    #creating a empty dictionare [freq] that will be used to store the number of each word
    #count the frequency of each word
    #[p] will turn in each value of

    l1 = frase.split()
    # dividir a frase em palavras e adicionar a uma lista
    
    frequencia = {}
    # dicionário vazio que será usado para armazenar a contagem de cada palavra
    
    # Contar a frequência de cada palavra
    for p in l1:
    # [p] se transformará em cada valor que esta dentro da lista [l1]
       
        if p in frequencia:
        # Se [p] já estiver no dicionário, incrementar a contagem
            frequencia[p] += 1
        
        else:
            frequencia[p] = 1
            # Caso contrário, adicionar a palavra ao dicionário com contagem 1
            #frequencia[p] = adiciona [p] ao dicionario
    
    return frequencia

# Exemplo de uso
frase =input("type the sentence: ")

resultado = contar_frequencia_palavras(frase)

# Exibir o resultado
print("-"*15)
print("Frequência de palavras:")
for p, contagem in resultado.items():

    print(f"{p}: {contagem}", end="    ")
    print("")
print("-"*15)