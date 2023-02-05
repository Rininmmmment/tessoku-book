N = int(input())
num = 10**9 + 7

A = [0] * N
A[0], A[1] = 1, 1
for i in range(2, N):
    A[i] = (A[i-1] + A[i-2]) % num
print(A[N-1])