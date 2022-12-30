text=input().split()
n=int(text[0])
q=int(text[1])
lista=input().split(" ")
listb = [ int(x) for x in lista ]


text=[]
for h in range(0,q):
    i=input()
    text.append(i)

    

dic={}
dic[0]=listb.count(0)
for j in range(1,max(listb)+1):
    dic[j]=listb.count(j)+dic[j-1]
    
for x in text:
    if x>max(listb):
        print(dic[max(listb)])
    else:    
        print(dic[x])    
        
        