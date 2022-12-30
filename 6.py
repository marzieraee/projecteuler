

text=input().split()
n=int(text[0])
lista=input().split(" ")
listb = [ int(x) for x in lista ]
ANS = []
for i in range (n-1):
    c=0   
    for j in range (i,n):
        c += listb[j]
        ANS.append(c)
if ANS == 0 :
    ANS = max(listb)            
            
            

print(max(ANS))






n = int(input())
a = list(map(int, input().split()))

ans = -10**9 * 1000

for l in range(n):
    s = 0
    for r in range(l, n):
        s += a[r]
        if s > ans:
            ans = s

print(ans)