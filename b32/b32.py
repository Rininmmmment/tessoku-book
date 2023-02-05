N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (N+1)

for i in range(N+1):
    for j in range(K):
        if A[j] <= i and dp[i-A[j]] == False:
            dp[i] = True

if dp[N] == True:
    print("First")
else:
    print("Second")