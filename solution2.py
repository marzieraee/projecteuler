max=4000000
b=0
list1=[0,1]

while b<max:
     value=b+list1[-2]
     if value<=max:
        list1.append(value)
        b=value
     elif value>max:
         break
list2=[]
for i in list1:
    if (i%2)==0 :
        list2.append(i)
   
print(sum(list2))

