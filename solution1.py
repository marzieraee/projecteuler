max=1000
a=3
b=5
list1=0

while b<max:
    list1+=b
    b+=5

while a<max :
    list1+=a
    a+=3
for i in range(1000) :
    if i%3==0 and i%5==0 :
        list1 -=i


print(list1)


