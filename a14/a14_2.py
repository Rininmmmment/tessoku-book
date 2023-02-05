import bisect
import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

P, Q = [], []
for i in range(N):
    for j in range(N):
        P.append(A[i] + B[j])
        Q.append(C[i] + D[j])
Q.sort()
# print(P, Q)

for i in range(N**2):
    index = bisect.bisect_left(Q, K-P[i])
    if index < N**2 and Q[index] == K-P[i]:
        print('Yes')
        sys.exit(0)
print('No')