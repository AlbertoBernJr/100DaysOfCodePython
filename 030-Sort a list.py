# Sort a list of numbers in ascending order


list=input("Type the values separated by spaces.: ")
# recebe os valores da variavel [list]
# Get the values and store them in the variable [list].

list=list.split()
# transform the variable [list] into a list
# Transform the variable [list] into a list.

listsorted=sorted(list)
# usando a função [sorted()]
# Use the function [sorted()].

print(f"normal list: {list}")
print(f"sorted list: {listsorted}")