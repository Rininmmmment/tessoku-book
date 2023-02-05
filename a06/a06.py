# 入力
N, Q = map(int, input().split())
A = list(map(int, input().split()))
L, R = [None] * Q, [None] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())

# 来場者数の累積和を求める
S = [0] * (N+1)    # 0日目, 1日目, ..., N日目の累積和
for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]

for i in range(Q):
    Answer = S[R[i]] - S[L[i]-1]
    print(Answer)