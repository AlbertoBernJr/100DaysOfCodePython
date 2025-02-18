"""
Write a function to check if a given string is a palindrome.
"""

import re

def palindrome(x):
    FormatedString = re.sub(r'[^a-zA-Z0-9]', '', x).lower()
    # remove all excess words and numbers
    # [.lower()] = convert to lowercase
    return FormatedString == FormatedString[::-1]
    #create an inverted version of the text
    # [::-1] = examine all the words from back to front

x=input("enter with a word or number: ")
print("-"*5)
print(palindrome(x))
print("-"*5)