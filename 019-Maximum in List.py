# Write a function to find the maximum element in a list

def MaxValue(list1):
    if not list1:
        return "The list is empty"
    
    max = list1[0]  
    # Passo 1: Assume que o primeiro elemento é o maior
    # Assume that the first value is the largest.

    for n in list1:  
    # Passo 2: Itera sobre cada elemento da lista
    # The variable [n] takes the form of each element in [list1].

        if n > max:  
        # Passo 3: Compara o elemento atual com o máximo atual
        # Compare the current max value with the next value.

            max = n  
            # Passo 4: Atualiza o máximo se o elemento atual for maior
            # Update the max value if the next value is larger.
    
    return max  
    # Passo 5: Retorna o maior elemento encontrado
    # Return the largest value.


num=int(input("how many values do you want to add to the list?: "))
# pergunta ao usuário quantos numeros ele quer adicionar a lista
# ask the user how many values wants to add to the list

list1 = []
# Criar uma lista inicial com alguns números
# create an initial list

for i in range(0,num):
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
print(f"the max value: {MaxValue(list1)}")
# mostra a soma dos numeros que estão na [list1]
# show the sum of the numbers in [list1]
print("-"*15)