#Write a function to reverse a list.

def listRv(x):
    list=[]
    # ja foi criada a lista na qual os valores serão adicionados
    # The list where the values will be stored has been created

    n=int(input("enter with the number limit of values: "))
    # variavel [n] irá conter o numero de valores limites que o usuario quer ver
    # The variable [n] will store the limited number of values that the user wants to see

    for i in range(0,n):
        list2=int(input(f"type the {i+1}° number: "))
        list.append(list2)
        # adicionando o valor da [list2] para a [list]
        # Add the value from [list2] to [list]

    listRv=list[::-1]
    # [::-1] = técnica de slicing que percorre a lista do início ao fim, mas com um passo de [-1], o que 
        # inverte a ordem dos elementos.
    # [::-1] = A slicing technique that goes through the list from start to end with a step of [-1], reversing 
        # the order of the values

    return listRv

print(listRv(list))