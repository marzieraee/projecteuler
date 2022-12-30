from json.encoder import INFINITY


text=input().split()
n=int(text[0])
lista=input().split(" ")
listb = [ int(x) for x in lista ]

listb.sort()

ANS=INFINITY
if n%2==0:
    m=listb[int((n/2)+1)]
elif n==1:
    m=listb[0]
else:
    m=listb[int((n+1)/2)]
        
c=0 
for i in range(n):
    if n==1:
       c=0
    c+=abs(listb[i]-m)
    
print(m,c)