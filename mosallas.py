a , b , c = [int(a) for a in input().split()]
if a==0 or b==0 or c==0 or a+b+c!=180 :
    print('No')
elif a+b+c == 180 :
    print('Yes')


