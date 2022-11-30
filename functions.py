list1 = [1,2,3,4,5]

#filter
#filter()

#reversed()
for i in reversed(list1) :
    print(i , end=' ')

#sorted
print(f'\n{sorted(list1)}')

#map
def f(x):
    return int(x)
ls = [2, '4', False, 3.14]
#map(f, ls)
#<map object at 0x00B77F90>
for x in map(f, ls):
    print(x, end=' ')
for x in map(int, ls):
    print(x, end=' ')