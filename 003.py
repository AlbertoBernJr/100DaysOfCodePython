"""
Basic Input and Output:
Write a program that reads a single input from the user and prints 
it to the console. For example, if the user enters their name, the program 
should output: ""Hello, {name}""

Handling Different Data Types:
Extend the program to read and print different types of inputs. Ensure the 
inputs are properly converted to their respective types and then printed. 
The program should ask the user to enter:
"""

nome=input("seu nome: ")

idade=int(input("sua idade: "))

altura=float(input("sua altura: "))
print("")

print("Informações:")
print(f"nome: {nome} - tipo: {type(nome)}")
print(f"idade: {idade} - tipo: {type(idade)}")
print(f"altura: {altura}, tipo: {type(altura)}")