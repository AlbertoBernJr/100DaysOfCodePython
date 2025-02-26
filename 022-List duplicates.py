# Write a function to remove duplicates from a list


listNDup=[]
listDup=[]

n=int(input("enter with the number limit of values: "))

for i in range(0,n):
    list2=int(input(f"type the {i+1}° number: "))
    listDup.append(list2)
    
for j in listDup:
    if j not in listNDup:
        listNDup.append(j)

print("-"*10)
print(f"Original list: {listDup}")
print("-"*10)
print(f"Whithout duplicates list: {listNDup}")
print("-"*10)
