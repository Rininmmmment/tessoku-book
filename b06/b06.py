N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L, R = [None] * Q, [None] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())

# 累積和を計算する
S = [0] * (N+1)    # 0回目、1回目、...、N回目までの累積和
for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]
# print(S)

# 答えを計算する
for i in range(Q):
    win_count = S[R[i]] - S[L[i]-1]
    lose_count = R[i] - L[i] + 1 - win_count
    # print(win_count, lose_count)
    if win_count > lose_count:
        print("win")
    if win_count < lose_count:
        print("lose")
    if win_count == lose_count:
        print("draw")