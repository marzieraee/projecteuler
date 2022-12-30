n = int(input())
lista = input().split(" ")
listb = [ int(x) for x in lista ]
for i in range(len(listb)-1) : 
    for j in range(len(listb)-1):
        if listb[j] > listb[j+1]:
            listb[j] , listb[j+1] = listb[j+1] , listb[j]

for num in listb:
    print(num, end = " ")