n = int(input())
ans = set()

for a in range (1,n):
    for b in range (a,n-a):
            
        c = n - a - b
        if a + b > c and c >= b:
    
            x=(a,b,c)
            ans.add(tuple(sorted(x)))
            

print(len(ans))                
