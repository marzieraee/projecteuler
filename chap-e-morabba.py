n = int(input())
list=['*',' ','*']
for i in range(n):
    if i==0 :
        print(list[0]*n)
    elif i in range(1,n-1) :
        print(list[0]+list[1]*(n-2)+list[-1])
    else :
        print(list[0]*n)