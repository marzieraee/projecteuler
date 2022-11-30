def calc(a) :
    max1 = max(a)
    sum1 = sum(a)
    l1 = len(a)
    mean1 = sum1/l1
    return (mean1 , max1) 
print(calc([1,2,3,4]))