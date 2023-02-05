N, K = map(int, input().split())

Answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        z = K - i - j
        if z > 0 and z <= N:
            Answer += 1

print(Answer)