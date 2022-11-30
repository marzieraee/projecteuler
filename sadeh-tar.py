list=[]
sum = 0
Product = 1
for i in range(4) :
    x = int(input())
    list += [x]
    sum += x
    Product *= x
Average = sum/4
print('Sum : %.6f'%sum)
print('Average : %.6f'%Average)
print('Product : %.6f'%Product)
print('MAX : %.6f'%max(list))
print('MIN : %.6f'%min(list))