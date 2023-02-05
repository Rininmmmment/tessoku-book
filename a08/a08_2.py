H, W = map(int, input().split())
X = []
for i in range(H):
    X.append(list(map(int, input().split())))
Q = int(input())
A, B, C, D = [0] * Q, [0] * Q, [0] * Q, [0] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = list(map(int, input().split()))

# 累積和を計算する（横）
S = [[0]*(W+1) for i in range(H+1)]    # (0, 0), (0, 1), ..., (H, W)までの累積和
for i in range(1, H+1):
    for j in range(1, W+1):
        S[i][j] = S[i][j-1] + X[i-1][j-1]

# 累積和を計算する（縦）
for i in range(1, H+1):
    for j in range(1, W+1):
        S[i][j] = S[i-1][j] + S[i][j]

# 答えを計算する
for i in range(Q):
    Answer = S[C[i]][D[i]] - S[A[i]-1][D[i]] - S[C[i]][B[i]-1] + S[A[i]-1][B[i]-1]
    print(Answer)