N = int(input())
h = list(map(int, input().split()))

# 動的計画法
dp = [ 0 ] * (N+1) # i段目に辿り着くための最小コスト
dp[1] = abs(h[0] - h[1])
# dp[2] = abs(h[2] - h[2])

for i in range(2, N):
	# dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])
    dp[i] = min(dp[i-1]+abs(h[i-1]-h[i]), dp[i-2]+abs(h[i-2]-h[i]))

# 出力
print(dp[N-1])