N, H, W = map(int, input().split())
A, B = [None] * N, [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

C = A + B
XOR = 0
for i in range(2*N):
    XOR = (XOR ^ (C[i]-1))

if XOR != 0:
    print("First")
else:
    print("Second")