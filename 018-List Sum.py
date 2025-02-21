"""
Write a function to find the sum of all elements in a list.
"""

def SumList(list2):
    sum = 0
    # Inicializa a variável para armazenar a soma
    # create a variable to store the sum
    
    for value in list1:
    # Itera sobre cada valor da lista
    # [value] take form of each value of [list1]
        
        sum = sum + value
        # Adiciona o valor à soma
        # add the [value] to the [sum]
    
    return sum

n=int(input("how many values do you want to add to the list?: "))
# pergunta ao usuário quantos numeros ele quer adicionar a lista
# ask the user how many values wants to add to the list

list1 = []
# Criar uma lista inicial com alguns números
# create an initial list

for i in range(0,n):
    list2 = int(input("add a new number to the list: "))
    # Pedir ao usuário para digitar um número para adicionar à lista
    # ask the user for the number they want to add to the list

    list1.append(list2)
    # Adicionar o número digitado à lista
    # add the typed number to the list

print("-"*27)
print("Updated list",list1)
# Mostrar a lista atualizada
# show the updated list

print("-"*27)
print(f"sum of the values: {SumList(list2)}")
# mostra a soma dos numeros que estão na [list1]
# show the sum of the numbers in [list1]
print("-"*15)
 






