"""
Write a function to check if a given string is a palindrome.
"""

import re

def palindrome(x):
    FormatedString = re.sub(r'[^a-zA-Z0-9]', '', x).lower()
    # remove all excess words and numbers
    #remove todas as letras e numeros excessivos

    # [.lower()] = convert to lowercase
    # [.lower()] = transforma em letras minúscula

    return FormatedString == FormatedString[::-1]
    # create an inverted version of the text
    # cria uma versão inversa do texto

    # [::-1] = examine all the words from back to front
    # [::-1] = verifica todas as palavras de tras para frente

x=input("enter with a word or number: ")
print("-"*5)
print(palindrome(x))
print("-"*5)