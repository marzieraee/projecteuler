a , b , c = [int(x) for x in input().split()]
if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a :
    print('Yes')
else :
    print('No')