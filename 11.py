from json.encoder import INFINITY


n = int(input())
lista = input().split(" ")
seq = [ int(x) for x in lista ]

maxi = -INFINITY
tem = 0
for i in range(0, n):
    tem = max(seq[i], tem+seq[i])
    maxi = max(maxi, tem) 
    
print(maxi)

