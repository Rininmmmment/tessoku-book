N = int(input())
A = list(map(int, input().split()))
D = int(input())
L, R = [None] * D, [None] * D
for i in range(D):
    L[i], R[i] = map(int, input().split())

# 累積max
P = [0] * N
P[0] = A[0]
for i in range(1, N):
    P[i] = max(P[i-1], A[i])

Q = [0] * N
Q[N-1] = A[N-1]
for i in reversed(range(N-1)):
    Q[i] = max(Q[i+1], A[i])

for i in range(D):
    print(max(P[L[i]-1-1], Q[R[i]+1-1]))