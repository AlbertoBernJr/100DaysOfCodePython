#Reverse words in a sentence

n=input("frase: ")

def RevSet(x):
    list=n.split()
    RevList=list[::-1]

    let=" ".join(RevList)
    
    print("-"*20)
    print(f"lista normal: {list}")
    print(f"frase normal: {n}")
    print("-"*20)
    print(f"lista reversa: {RevList}")
    print(f"frase reversa: {let}")

RevSet(n)