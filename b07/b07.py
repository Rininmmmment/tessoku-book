T = int(input())
N = int(input())
L, R = [None] * N, [None] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

# 増減を記録する
A = [0] * (T + 1)    # 0〜1時、1〜2時、...、T〜T+1時の増減
for i in range(N):
    A[R[i]] -= 1
    A[L[i]] += 1
# print(A)

# 累積和の計算
S = [0] * (T + 1)    # 0〜1時、1〜2時、...、T〜T+1時の出勤人数
for i in range(1, T+1):
    S[i] = S[i-1] + A[i-1]

for i in range(1, T+1):
    print(S[i])