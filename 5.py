

text=input().split()
n=int(text[0])
lista=input().split(" ")
listb = [ int(x) for x in lista ]
ANS= 0
for i in range (1,n+1):
    for j in range (i):
        c=0   
        for x in range (j,i+1):
            c +=listb[x]
        if c>ANS:
            ANS=c
if ANS ==0:
    ANS=max(listb)            
            
            

print(ANS)



# n = int(input())
# a = list(map(int, input().split()))

# ans = -10**9 * 100

# for r in range(1, n + 1):
#     for l in range(r):
#         s = 0
#         for i in range(l, r):
#             s += a[i]
        
#         if ans < s:
#             ans = s

# print(ans)