D = int(input())
N = int(input())
L, R = [None] * N, [None] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

# 増減を記録する
A = [0] * (D+2)    # 0日目、...D+1日目
for i in range(N):
    A[R[i]+1] -= 1
    A[L[i]] += 1

# 累積和を計算する
S = [0] * (D + 1)    # 0日目、1日目、...、D日目
for i in range(1, D+1):
    S[i] = S[i-1] + A[i]

# 答え
for i in range(1, D+1):
    print(S[i])