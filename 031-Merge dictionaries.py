#Merge two dictionaries

Identific1=["nome", "idade", "estado"]
Resps=[]
NumIdentific1=len(Identific1)

for i in range(0, NumIdentific1):
    R=input(f"{Identific1[i]}: ")
    Resps.append(R)

Dic= dict(zip(Identific1, Resps))
print(Dic)



