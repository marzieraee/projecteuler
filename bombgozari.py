n , m = map(int , input().split())
row = [ 0 * m for m]
k = int(input('k = '))

for i in range(k) : 
    x , y = map(int , input().split())
    list1 = [x , y]

for i in range(n) :
    for j in range(m) :
        if i==x and j==y :
            print('*' , end=' ')
        else :
            print(0 , end=' ')
    print(f'\n')