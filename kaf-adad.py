n , k = map(float,input().split())
a = n/(2**k)
if a == int(a) :
    print(a)
else :
    if a<0 :
        print(int(a)-1)
    else :
        print(int(a))