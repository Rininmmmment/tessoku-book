N = int(input())
A = list(map(int, input().split()))    # 端から1部屋目, 2部屋目...N部屋目
D = int(input())
L, R = [None] * D, [None] * D    # 1日目, 2日目, 3日目...D日目
for i in range(D):
    L[i], R[i] = map(int, input().split())

# 左側、右側の累積最大
P, Q = [0]*N, [0]*N    # 端から1部屋目, 2部屋目...

# i部屋目までの累積最大を求める
P[0] = A[0]
for i in range(1, N):
    P[i] = max(P[i-1], A[i])

Q[N-1] = A[N-1]
for i in reversed(range(0, N-1)):
    Q[i] = max(Q[i+1], A[i])
# print(P, Q)

for i in range(D):
    l_max = P[L[i]-2]
    r_max = Q[R[i]]
    print(max(l_max, r_max))