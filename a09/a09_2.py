H, W, N = map(int, input().split())
A, B, C, D = [None] * N, [None] * N, [None] * N, [None] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 差分を記録する
S = [[0]*(W+2) for i in range(H+2)]    # (0,0), ..., (H,W)の差分
for i in range(N):
    S[A[i]][B[i]] += 1
    S[A[i]][D[i]+1] -= 1
    S[C[i]+1][B[i]] -= 1
    S[C[i]+1][D[i]+1] += 1

# 累積和をとる（横）
for i in range(1, H+2):
    for j in range(1, W+1):
        S[i][j] = S[i][j-1] + S[i][j]

# 累積和をとる（縦）
for i in range(1, H+2):
    for j in range(1, W+1):
        S[i][j] = S[i-1][j] + S[i][j]

for i in range(1, H+1):
    print(*S[i][1:W+1])