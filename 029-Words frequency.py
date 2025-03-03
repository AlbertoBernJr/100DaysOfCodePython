# Create a dictionary of words and their frequencies

x=input("phrase: ")
x=x.lower()
# diminui todas as letras dentro da variavel [x]
# All the words inside the variable [x] will be converted to lowercase.


def DicFreq(x):
    listW=[]
    # criando a lista que irá guardar as palavras
    # Creating the list that will store the words.

    dic={}
    #criando dicionario
    # Creating a dictionary.

    listW=x.split()
    # adicionando todos os valores de [x] na lista [listW]
    # Add all the [x] values to the list [listW].

    for i in listW:
    # a variavel [i] se transformará nos valores da lista [listW]
    # The [i] variable will take the form of the [listW] values.

        if i in dic:
            dic[i]+=1
            #Se [i] já estiver no dicionário, incrementar a contagem
            # If [i] is already in the dictionary, increment its count by 1.

        else:
            dic[i]=1
            # Caso contrário, adicionar a palavra ao dicionário com contagem 1
            # Otherwise, add the word [i] to the dictionary with a count of 1.
            # adiciona [i] ao dicionario


    print(dic)

DicFreq(x)
