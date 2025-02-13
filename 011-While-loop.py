#Use a while loop to print even numbers from 2 to 20.

n=2
print("Even numbers between 2 and 20: ")
while n<21:
    if n%2==0:
        print(n,end=" ")
    n=n+1
