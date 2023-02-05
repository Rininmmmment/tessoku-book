N = int(input())
X, Y = [None] * N, [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
Q = int(input())
A, B, C, D = [None] * Q, [None] * Q, [None] * Q, [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 点の位置を記録する
Z = [[0]*1501 for i in range(1501)]    # (0,0), ..., (1500, 1500)の点
for i in range(N):
    Z[X[i]][Y[i]] += 1

# 累積和をとる（横）
for i in range(1, 1501):
    for j in range(1, 1501):
        Z[i][j] = Z[i][j-1] + Z[i][j]

# 累積和をとる（縦）
for i in range(1, 1501):
    for j in range(1, 1501):
        Z[i][j] = Z[i-1][j] + Z[i][j]

# 答えを計算する
for i in range(Q):
    Answer = Z[C[i]][D[i]] - Z[C[i]][B[i]-1] - Z[A[i]-1][D[i]] + Z[A[i]-1][B[i]-1]
    print(Answer)