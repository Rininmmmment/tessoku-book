N, A, B = map(int, input().split())

dp = [False] * (N+1)

for i in range(N+1):
    if A <= i and dp[i-A] == False:
        dp[i] = True
    elif B <= i and dp[i-B] == False:
        dp[i] = True
    else:
        dp[i] = False

if dp[N] == True:
    print("First")
else:
    print("Second")