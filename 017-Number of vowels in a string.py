#Write a function to count the number of vowels in a string.
# escreva uma função que conte o numero de vogais numa string

def VowelsCount(x):
    
    vowels = "aeiouAEIOU"
    # criando uma Lista de vogais
    # creating a list of vowels
    
    counter = 0
    # creating a vowel counter
    # Inicializa o contador de vogais
    
    for caractere in x:
    # the variable [caractere] will take the form of each character in [texto]
    # a variavel [caractere] toma forma de todas as palavras de [x]

        # Verifica se o caractere é uma vogal
        if caractere in vowels:
        # check if the variable [caractere] is in the vowel list [vowels] 
        # verifica se a variavel [caractere] esta dentro da lista [vowels]
            counter += 1  # Incrementa o contador
            # se for verdade, o [counter] será auemntado em 1
            # if true, the counter will increment by 1
    
    return counter

x=input("ente with a value: ")
print(f"the value [{x}] has [{VowelsCount(x)}] vowels")