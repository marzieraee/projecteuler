def func(a=3, b=2):
    return print(a*b)
func(3,3)

def func2(a=3 , list1=[]) :
    list1.append(a)
    return print(list1)
func2(2)

def s(a , *b) :
    return sum(b)
print(s(1,2,3,4))

def saeed(*args,**kwargs) :
    print(args)
    print(kwargs)
    return args , kwargs
saeed(1,2,3,v=1,n=2,m=3,z=4)


print(*(1,2,3))
print(*[1,2,3])
print(*{'a':1,'b':2,'c':3})