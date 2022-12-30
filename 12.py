# import sys
# sys.setrecursionlimit(1000000)
# n = int(input())

# def cal(x):
#     temp = cal(x-1)
#     if x % 2 == 0:
#         if x == 0:
#             return 5
        
#         return temp-21
#     else:
        
#         return temp*temp

# print(cal(n))


import sys
sys.setrecursionlimit(10**6)

def  f(i):
    #Base Condition
    if i==0:
        return 5
    #Compute f(i-1) and put it into 'temp'
    temp=f(i-1)
    if i%2==0:
        return temp-21
    else:
        return temp*temp

n=int(input())
print(f(n))