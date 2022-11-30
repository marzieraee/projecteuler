n = int(input())
fibo_list = [1 , 2]
for i in range(1,n+1) :
    fibo_list+=[fibo_list[i-1]+fibo_list[i]]
for i in range(1,n+1) :
    if i in fibo_list :
        print('+',end='')
    else :
        print('-',end='')
