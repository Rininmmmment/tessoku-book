N = int(input())
X, Y = [None] * N, [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
Q = int(input())
A, B, C, D = [None] * Q, [None] * Q, [None] * Q, [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

Z = [[0] * 1500 for i in range(1500)]
for i in range(N):
    Z[X[i]-1][Y[i]-1] += 1

# 累積和をとる
S = [[0] * 1501 for i in range(1501)]
for i in range(1, 1501):
    for j in range(1, 1501):
        S[i][j] = S[i][j-1] + Z[i-1][j-1]

for i in range(1, 1501):
    for j in range(1, 1501):
        S[i][j] = S[i][j] + S[i-1][j]

for i in range(Q):
    print(S[C[i]][D[i]] + S[A[i]-1][B[i]-1] - S[C[i]][B[i]-1] - S[A[i]-1][D[i]])