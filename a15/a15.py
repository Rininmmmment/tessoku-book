import bisect

N = int(input())
A = list(map(int, input().split()))

X = list(set(A))
X.sort()

B = [0] * N
for i in range(N):
    index = bisect.bisect_left(X, A[i])
    B[i] = index + 1

print(*B)