text=input().split()
n=int(text[0])
q=int(text[1])
lista=input().split(" ")

text=[]
for h in range(0,q):
    i=input()
    text.append(i)
for c in text:
    j=int(c)
    
    setx=list()
    for m in range(0,n):
        v=(int(lista[m]))
        if v<j:
            setx.append(v)
    print(len(setx))



    
        
        