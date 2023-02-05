N = int(input())
A = list(map(int, input().split()))

XOR = A[0]
for i in range(1, N):
    XOR = (XOR ^ A[i])

if XOR == 0:
    print("Second")
else:
    print("First")