"""
If-else Statements
Write a program that takes an integer as input and checks if 
it's even or odd.
Write a program that takes an age as input and determines if 
the person is a child, teenager, adult, or senior citizen.

Nested If-else Statements
Using nested if-else, write a program that takes three 
numbers as input and determines the largest among them.

For Loop
Write a program to calculate the sum of all numbers up to the 
given input number.

While Loop
Write a program to calculate the factorial of a given number.

"""
n1=int(input("entre com um número: "))
if n1%2 == 0:
    print(f"o numero {n1} é par")
else:
    print(f"o numero {n1} é ímpar")
print("-"*15)

idade=int(input("idade: "))
if idade > 17:
    print("voce é maior de idade com:", idade,"anos")
else:
    print("voce é menor de idade com:", idade,"anos")
print("-"*15)


num1=int(input("1 numero: "))
num2=int(input("2 numero: "))
num3=int(input("3 numero: "))
if num1>num2 and num1>num3:
    print("maior numero: ",num1)
elif num2>num1 and num2>num3:
    print("maior numero: ", num2)
else:
    print("maior numero: ", num3)

print("-"*15)
num4=int(input("numero: "))
soma=0
for n in range(1,num4+1):
    soma=soma+n
print(f"soma dos numeros anteriores até o {num4} é: {soma}")

print("-"*15)
num5=int(input("numero: "))
fatorial=1
while num5>1:
    fatorial=fatorial*num5
    num5=num5-1
print(f"o fatorial de {num5} é {fatorial}")