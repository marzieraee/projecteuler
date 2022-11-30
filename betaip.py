n , m = map(int , input().split())
k = int(input('k = '))

for i in range(k) : 
    x , y = map(int , input().split())

 
for i in range(n) :
    for j in range(m) :
        if i!=x and j!=y :
            print(0 , end=' ')
        else :
            print('*' , end=' ')
    print(f'\n')