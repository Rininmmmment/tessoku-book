import bisect
import sys

def bittansaku(A):
    sumlist = []
    for i in range(2**len(A)):
        sum = 0
        for j in range(len(A)):
            wari = 2 ** j
            if (i // wari) % 2 == 1:
                sum += A[j]
        sumlist.append(sum)
    return sumlist

N, K = map(int, input().split())
A = list(map(int, input().split()))

L = A[:N//2]
R = A[N//2:]

P = bittansaku(L)
Q = bittansaku(R)

Q.sort()

for i in range(len(P)):
    index = bisect.bisect_left(Q, K-P[i])
    if index < len(Q) and Q[index] == K-P[i]:
        print('Yes')
        sys.exit()
print('No')