﻿from random import*
arvud=[] 
kogus=int(input("kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
print(arvud)
max_arv=max(arvud)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=round(max_arv/kogus,3)
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)




arvud=[] 
kogus=int(input("kogus: "))
for i in range(kogus):
    arvud.append(randint(1,100))
print(arvud)
osa1=[]
osa2=[]
print(arvud)
if len(arvud)%2==0 and len(arvud)>=2:
    n=int(len(arvud)/2)
    for i in range(1,n+1):
        osa1.append(arvud[i-1])
    for j in range(n+1,len(arvud)+1):
        osa2.append(arvud[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2) 
else:
    print("Viga!")




index=" "
maakonnad=["Tln","NArva","K-Järve", "Ida-Virumaa", "Tartu", "Viljandi", "Parnumaa", "Saaremaa"]
while True:
    try:
        index=int(input("Anna index: "))
        if index<99999 and index<10000:
            break
    except:
         print("Anna õige index!")
i=index//10000 #1,2,3,4,5,6,7,8,9
print(f"{index} on {maakonnad}[i-1]") #0,1,2,3,4,5,6,7,8
if i in[1,2,3]:
    print("jääta kodus!")
else:
    print("Kanna maski!")





      