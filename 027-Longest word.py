# Find the longest word in a sentence

f=input("uma frase: ")

def Longest(f):
    f=f.lower()

    listF=f.split()
    listF2="".join(listF)
    listNum=[0]

    Qtd1=len(listF)
    Qtd=len(listF2)

    for n in listF:
        num=len(n)
        listNum.append(num)

    maior=listNum[0]
    for max in listNum:
        if maior<max:
            maior=max

    posicao=listNum.index(maior)
    posicao=posicao-1
    print(f"numero de cada elemento: {listNum}")
    print(f"cada elemento: {listF}")
    print(f"maior numero: {maior}")
    #print(f"a posição do maior elemnto: {posicao} ")
    
    print(f"maior elemento: {listF[posicao]}")
    

Longest(f)