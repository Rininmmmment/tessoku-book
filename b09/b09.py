# 座標かマスかの違いによってインデックスが変わる。
# 与えられた具体例について図を書いてからコードを書き始める。

N = int(input())
A, B, C, D = [None] * N, [None] * N, [None] * N, [None] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

# 累積和をとる
Z = [[0] * 1501 for i in range(1501)]
for i in range(N):
    Z[A[i]][D[i]] -= 1
    Z[C[i]][B[i]] -= 1
    Z[C[i]][D[i]] += 1
    Z[A[i]][B[i]] += 1

# 縦方向の累積和
for i in range(0, 1501):
    for j in range(1, 1501):
        Z[i][j] = Z[i][j-1] + Z[i][j]

# 横方向の累積和
for i in range(1, 1501):
    for j in range(0, 1501):
        Z[i][j] = Z[i-1][j] + Z[i][j]

answer = 0
for i in range(1501):
    for j in range(1501):
        if Z[i][j] >= 1:
            answer += 1

print(answer)