#Create a simple calculator program that can add, subtract, multiply, and divide two integers

calculo=int(input("escolha o calculo que deseja realizar -> soma=1 | subtração=2 | divisão=3 | multiplicação=4: "))
print("-"*15)

n1=int(input("1° número: "))
n2=int(input("2° número: "))
print("-"*15)

if calculo == 1:
    resultado=n1+n2
    print(f"{n1} + {n2} = {resultado}")
elif calculo == 2:
    resultado=n1-n2
    print(f"{n1} - {n2} = {resultado}")
elif calculo == 3:
    resultado=n1/n2
    print(f"{n1} / {n2} = {resultado}")
else:
    resultado=n1*n2
    print(f"{n1} x {n2} = {resultado}")