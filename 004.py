"""
Day 4: Basic Operators and Expressions
Arithmetic Operators
Write a program to perform the following arithmetic operations using two numbers:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Floor Division (//)
Modulus (%)
Exponentiation (**)


Relational Operators
Write a program to compare two numbers using the following operators:
Equal to (==)
Not equal to (!=)
Greater than (>)
Less than (<)
Greater than or equal to (>=)
Less than or equal to (<=)


Logical Operators
Write a program that evaluates the following between 2 booleans(True or False):
Logical AND (and)
Logical OR (or)
Logical NOT (not)
"""
n1=1
n2=2

print("Operaçoes aritméticas")
print("Addition (1+2):", n1+n2)
print("Subtraction (1-2):", n1-n2)
print("Multiplication (1x2):", n1*n2)
print("Division (1/2):", n1/n2)
print("Floor Division:", n1//n2)
print("Modulus:", n1%n2)
print("Exponentiation (1^2):", n1**n2)

print("-"*15)

print("Relational Operators")
print("1 é igual a 2?:", 1==2)
print("1 é diferente de 2?:", 1!=2)
print("1 é maior do que 2?:", 1>2)
print("1 é menor do que 2?:", 1<2)
print("1 é maior ou igual a 2?:", 1>=2)
print("1 é menor ou igual a 2?:", 1<=2)

print("-"*15)

true=True
false=False

print("Logical Operators")
print("True AND False:", true and false)
print("True AND True:", true and true)
print("False AND False:", false and false)
print("False AND True:", false and true)
print("+"*10)
print("True OR False:", true or false)
print("True OR True:", true or true)
print("False OR False:", false or false)
print("+"*10)
print("NOT true:", not true)
print("NOT false:", not false)