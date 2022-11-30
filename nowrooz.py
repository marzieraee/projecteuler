X = int(input())
N = int(input())
if N==0 :
    print('20')
elif N==7 :
    print(X)
elif N>7 or N<7 :
    if X-N<0:
        print('0')
    else :
        print(X-N)