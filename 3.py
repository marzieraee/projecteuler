from json.encoder import INFINITY


text=input().split()
n=int(text[0])
k=int(text[1])
lista=input().split(" ")
listb = [ int(x) for x in lista ]

ANS=INFINITY
for x in range(min(listb)-(n-1)*k,max(listb)):
    c=0
    for i in range(n):
        c+=abs(x+(i)*k-listb[i])
    if c<ANS:
        ANS=c
        

if ANS==INFINITY:
    ANS=0
print(ANS)
        
        