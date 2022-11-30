n=int(input())
a=input()
b=input()
for i in range(n) :
    if a[i]==b[i] :
        n-=1
print(n)