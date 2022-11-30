i = 0
list =[]
while i==0 :
    x = int(input())
    if x != 0 :
        list = list + [x]
    else :
        i=1
for j in list[::-1] :
    print(f'{j}')
