list=[]
count=0
for i in range(1,6) :
    n = input()
    if 'MOLANA' in n:
        list+=[str(i)]
    elif 'HAFEZ' in n:
        list+=[str(i)]
    else :
        count+=1
if count==5 :
    print("NOT FOUND!")
else :
     a = ' '.join(list)
     print(a)