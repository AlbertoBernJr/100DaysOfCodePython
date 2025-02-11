"""
1. Write a program that generates a random number. 
2. Write a program that generates random number between 2 integers
"""
import random

n1=int(input("1° number: "))
n2=int(input("2° number: "))
print("-"*15)

num1=random.randint(n1,n2)
print("the generated number is... ",num1)
print("-"*20)

num2=random.randint(10, 20)
print("beteween 10 and 20, the random number is: ",num2)