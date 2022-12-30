
from ntpath import join


n = int(input())
lista = input().split(" ")
listb = [ int(x) for x in lista ]
x = sorted(listb)
str1=""
for xi in x:
    str1 += str(xi) + " "
print(str1)




# n = int(input())
# A = list(map(int,input().split()))

# for i in range(len(A)):
     
#     # Find the minimum element in remaining
#     # unsorted array
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
             
#     # Swap the found minimum element with
#     # the first element       
#     A[i], A[min_idx] = A[min_idx], A[i]
    
# for num in A:
#     print(num, end = " ")