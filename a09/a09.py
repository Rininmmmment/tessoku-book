H, W, N = map(int, input().split())
A, B, C, D = [None] * N, [None] * N, [None] * N, [None] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 累積和を計算する
Z = [[0] * (W + 2) for i in range(H + 2)]
for i in range(N):
    Z[C[i]+1][D[i]+1] += 1
    Z[A[i]][B[i]] += 1
    Z[C[i]+1][B[i]] -= 1
    Z[A[i]][D[i]+1] -= 1

# 横の累積和
for i in range(1, H+2):
    for j in range(1, W+2):
        Z[i][j] = Z[i][j] + Z[i][j-1]

# 横の累積和
for i in range(1, H+2):
    for j in range(1, W+2):
        Z[i][j] = Z[i][j] + Z[i-1][j]

for i in range(1, H+1):
    print(*Z[i][1:W+1])

