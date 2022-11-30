n = int(input())
for i in range(n) :
    if i==int(n/2)+1 :
        print('*'*10)
    elif i<int(n/2)+1 :
        print
    for j in range(int(n/2)) :
        print('*')