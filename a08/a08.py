H, W = map(int, input().split())
X = []
for i in range(H):
    X.append(list(map(int, input().split())))
Q = int(input())
A, B, C, D = [None] * Q, [None] * Q, [None] * Q, [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

S = [[0] * (W+1) for i in range(H+1)]
for i in range(1, H+1):
    for j in range(1, W+1):
        S[i][j] = S[i][j-1] + X[i-1][j-1]

for i in range(1, H+1):
    for j in range(1, W+1):
            S[i][j] = S[i-1][j] + S[i][j]

for i in range(Q):
    print(S[C[i]][D[i]] + S[A[i]-1][B[i]-1] - S[C[i]][B[i]-1] - S[A[i]-1][D[i]])