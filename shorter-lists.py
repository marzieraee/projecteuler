list1 = [x*x for x in range(1,10)]
print(list1)

print()

list2 = [-5,0,5,4,100,142,-147,1]
list2 = [x for x in list2 if x<0]
print(list2)

print()

list3 = [(x,y) for x in range(1,4) for y in range(1,4) if x==y]
print(list3)

print()

matrix = [[1,2,3],[3,4,5],[6,7,8]]
for i in range(3) :
    for j in range(3) :
        print(matrix[i][j], end=' ')
    print()

print()

zeros=[[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        print(zeros[i][j] , end=' ')
    print()