#Write a function to calculate the Fibonacci sequence up to a certain limit.
#Escrever uma função para calcular a sequencia de fibonacci até um certo limite

n=int(input("enter with the number limit of values: "))
# variavel [n] irá conter o numero de valores limites que o usuario quer ver
# the variable [n] will store the limited number of values that the user wants to see

list=[1, 1]
# ja foi criado os 2 primeiros valores de Fibonacci
# the first two fibonacci values have alrready been created

for i in range(0,n-2):
    # [n-2] = diminuirá 2 valores da variável [n] porque já existem os 2 valores iniciais de fibonacci
    # [n-2] = will subtract 2 from the variable [n], which already existis in the fibonacci list

    list2=list[0+i]+list[1+i]
    # a medida que a variavel [i] for mudando de valor em sequencia, irá mudar a posição da lista
    # while the value of [i] is changes, it will also change the list position

    list.append(list2)
    # adicionando o valor da [list2] para a [list]
    # adding the [list2] value from [list2] to  [list]

print(list)