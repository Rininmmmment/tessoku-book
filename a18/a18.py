# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 動的計画法
# カード1〜iを使って話をjにできるか？
dp = [ [ None ] * (S + 1) for i in range(N + 1) ]
dp[0][0] = True
for i in range(1, S+1): # 0枚の時は全てFalse
	dp[0][i] = False

# カードiの数字を足したら和がjになるか？
for i in range(1, N+1):
	for j in range(0,S+1):
		if j < A[i-1]:
            # カードiなしですでに和がjならTrue
			if dp[i-1][j] == True:
				dp[i][j] = True
            # そうでなければA[i-1]を足してもjにならないのでFalse
			else:
				dp[i][j] = False

		if j >= A[i-1]:
            # すでに和がj、もしくはカードi-1までで和がj-A[i-1]ならTrue
			if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
				dp[i][j] = True
			else:
				dp[i][j] = False

# 出力
if dp[N][S] == True:
	print("Yes")
else:
	print("No")
