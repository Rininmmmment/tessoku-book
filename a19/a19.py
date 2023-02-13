# 入力
N, W = map(int, input().split())
w = [ None ] * (N + 1)
v = [ None ] * (N + 1)
for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())

# 動的計画法
# 品物1〜iの中から重さjになるように選んだとき、最大の価値
dp = [ [ -10 ** 15 ] * (W + 1) for i in range(N + 1) ]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(0,W+1):
        # 品物iを追加できない場合
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        # 追加できる場合、追加したものと追加しない場合の大きいほうにする
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])

# 出力
print(max(dp[N]))