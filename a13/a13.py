# 入力（A は 0 番目から始まることに注意）
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 差がKを超えないAのインデックスのうち、最大のもの
S = [0] * (N + 1)
R = [0] * (N - 1)

# 累積和
for i in range(1, N + 1):
    S[i] = S[i-1] + A[i-1]

# しゃくとり法
for i in range(0, N-1):
	# スタート地点を決める
	if i > 0:
		S[i] = S[i - 1]

	# ギリギリまで増やしていく
    # 配列の全てを探索する or 差がK以下の間
	while S[R[i]+1] - S[i] <= K and R[i] < N:
		R[i] += 1

print(R)
# # 出力
# Answer = 0
# for i in range(0, N-1):
# 	Answer += (R[i] - i)
# print(Answer)