n = input()
m = len(n)
list = list(n)
for i in range(0,m) :
    for j in range(i):
        list[j]=list[i]
    n = ''.join(list)
    print(n)