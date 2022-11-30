n = input()
m = input()
list1 = []
list2 = []
if n==m :
    print(f"{n} = {m}")

else :  
    for i in n :
        list1 += i
        n1 = int(''.join(list1[::-1]))
    for i in m :
        list2 += i
        m1 = int(''.join(list2[::-1]))
    if n1<m1 :
        print(f"{n} < {m}")
    else :
        print(f"{m} < {n}")
