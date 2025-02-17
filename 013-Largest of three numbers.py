#Write a program to find the largest of three numbers.

def MaiorNumero(n1,n2,n3):
    if (n1>n2)and(n1>n3):
        Maior=n1
    elif (n2>n1)and(n2>n3):
        Maior=n2
    else:
        Maior=n3

    print("-"*15)
    print("The largest is:", Maior)
    print("-"*15)


n1=int(input("1° number: "))
n2=int(input("2° number: "))
n3=int(input("3° number: "))

MaiorNumero(n1,n2,n3)
