from math import atan
from math import ceil, floor, gcd, radians
from math import pi
from math import tan


x = int(input('please enter a natural number : '))
if x <= 1 :
    print('enter a natural number between 0 < x < infinitive')
else :
    y = int(floor(pow(pi , 2 + atan(pow(radians(x),2)))))
    z = ceil(pow(x,5/3) + tan(x))
    print(gcd(z,y))