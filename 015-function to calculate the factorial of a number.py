#Write a function to calculate the factorial of a number.

n2=(int(input("enter with a number: ")))
n3=n2+1
2
n=0
fat=1
for i in range(1,n3):
#counting the numbers
    print(i, end=" ")
    n=n+1
    fat=fat*i
    if n<n2:
    #Determining the quantity of [+]
        for x in range(0,1):
        #[+] will be incremented until the condition is met
            print("x", end=" ")
    else:
    #when the condition is no longer met, it will display [=fat]
        print(f"= {fat}")

