# Write a function to convert a list of words into a sentence

def conv(n):
    n=n.split()
    # função [split()] = usado para separar os elementos e tornar-los elementos de uma lista
    # [split()] = Separates the values and transforms them into list elements.

    print("-"*15)
    print(f"list: {n}")
    
    print("-"*15)
    n="-".join(n)
    # ["-".join] = junta as palavras que estão na lista usando [-]
    # ["-".join] = Joins the words from the list using [-].

    print(f"Words joined together: {n}")
    print("-"*15)


n=input("Sentence: ")

conv(n)