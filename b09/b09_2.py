N = int(input())
A, B, C, D = [None] * N, [None] * N, [None] * N, [None] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())
S = [[0]*1501 for i in range(1501)]

# 差分を記録する
for i in range(N):
    S[A[i]][B[i]] += 1
    S[C[i]][D[i]] += 1
    S[A[i]][D[i]] = -1
    S[C[i]][B[i]] = -1

# 累積和（よこ）
for i in range(0, 1501):
    for j in range(1, 1501):
        S[i][j] = S[i][j] + S[i][j-1]

# 累積和（たて）
for i in range(1, 1501):
    for j in range(0, 1501):
        S[i][j] = S[i][j] + S[i-1][j]

Answer = 0
for i in range(1501):
    for j in range(1501):
        if S[i][j] >= 1:
            Answer += 1

print(Answer)