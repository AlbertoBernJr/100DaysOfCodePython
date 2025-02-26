#Write a function to find the intersection of two lists

def inters(l1, l2):
    #criando uma função que irá receber os resultados das 2 listas digitadas pelo usuario
    # Creating a function that will receive the result of the two lists typed by the user.

    list1=l1.split()
    # função [split()] = usado para separar os elementos e tornar-los elementos de uma lista
    # [split()] = Separates the values and transforms them into list elements.

    list1=set(list1)
    # função [set()] = transforma a lista em um conjunto que não permite repetição de valores
    # [set()] = Transforms the list into a set, which doesn’t allow duplicate values.

    list2=l2.split()
    list2=set(list2)

    intersecao = list1.intersection(list2)
    # [.intersection] = irá guardar os elementos em comum da [list2] e [list1]
    # [.intersection] = Stores the values that exist in both lists.

    inters =list(intersecao)
    # tranforma o resultado de [.intersection] em uma lista
    # Transform the result of [.intersection] into a list

    print("-"*15)
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")

    print("-"*15)
    print(f"Common values: {inters}")
    print("-"*15)

l1=input("lista1 - digite os elementos seperados por espaço: ")
l2=input("list 2 - digite os elementos seperados por espaço: ")

inters(l1, l2)
