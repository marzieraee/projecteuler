from datetime import date
sajjad = date(1999 , 1 , 14)
list1 = [sajjad.year , sajjad.month , sajjad.day]

person = input('enter their birthday in xxxx-xx-xx format : ')
date2 = person.split('-')
list2 = list(map(int , date2))

list3 = [(list2[0] - list1[0]) , (list2[1] - list1[1]) , (list2[2] - list1[2])]
print(list3)

if list3[0]< 0 :
    print('sajjad hanooz be donya naiamadeh')
elif list3[0]>0 and list3[1]<0 :
    print('sajjad hanooz be donya naiamadeh')
elif list3[0]>0 and list3[1]>0 and list3[2]<0 :
    print('sajjad hanooz be donya naiamadeh')
else :
    print(f''' year : {list3[0]}
    month : {list3[1]}
    day : {list3[2]} ''')