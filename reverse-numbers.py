list1 = []
for i in range(1000) :
    x = int(input('enter your number = '))
    list1.append(x)
    if x == 0 :
        list1.pop()
        break
for i in reversed(list1) :
    print(i , end=' ')