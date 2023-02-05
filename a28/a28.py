N = int(input())
T, A = [None]*N, [None]*N
for i in range(N):
    T[i], A[i] = input().split()

Answer = 0
for i in range(N):
    if T[i] == "+":
        Answer += int(A[i])
    if T[i] == "-":
        Answer -= int(A[i])
    if T[i] == "*":
        Answer *= int(A[i])
    if Answer < 0:
        Answer += 10000
    Answer %= 10000
    print(Answer)