
m=0
z=[600851475143]
for i in range(2,z[-1]):
    
    if z[-1]%i==0:
        
        x=z[-1]/i
        z.append(x)
        
    elif z[-1]==1:
         break
       
        
print(z[-2])