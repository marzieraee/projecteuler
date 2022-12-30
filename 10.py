n = int(input())
seq = [int(i) for i in input().split()]


for i in range(len(seq)) :
    p = i
    while p > 0 and seq[p] < seq[p-1] :
        seq[p-1] , seq[p] = seq[p] , seq[p-1]
        p = p-1

    




print(*seq, sep = " ")