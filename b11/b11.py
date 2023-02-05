import bisect

N = int(input())
A = list(map(int, input().split()))    # (index: 1, 2, ..., N)
A.sort()
Q = int(input())
X = [None] * Q    # (index: 1, 2, ..., Q)
for i in range(Q):
    X[i] = int(input())

for i in range(Q):
    answer = bisect.bisect_left(A, X[i])
    print(answer)