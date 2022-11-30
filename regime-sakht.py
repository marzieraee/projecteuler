a = input()
list = []
for ch in a :
    list+=ch
if list.count('R')>=3 :
    print('nakhor lite')
elif (list.count('R')>=2 and list.count('Y')>=2) :
    print('nakhor lite')
elif list.count('G')==0 :
    print('nakhor lite')
else :
    print('rahat baash')
        