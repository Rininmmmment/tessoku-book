N = int(input())
h = list(map(int, input().split()))

# 動的計画法
dp = [ 0 ] * (N) # i段目に辿り着くための最小コスト
dp[1] = abs(h[0] - h[1])
for i in range(2, N):
    dp[i] = min(dp[i-1]+abs(h[i-1]-h[i]), dp[i-2]+abs(h[i-2]-h[i]))

# print(dp)
# 復元
Answer = []
Place = N-1
while True:
	Answer.append(Place+1)
	if Place == 0:
		break

    # dpの値から、1個前にいた場所はどこなのか求める
	if dp[Place] == dp[Place-1]+abs(h[Place-1]-h[Place]):
		Place = Place - 1
	else:
		Place = Place - 2
Answer.reverse()

Answer2 = [str(i) for i in Answer]
print(len(Answer))
print(" ".join(Answer2))

# print(dp)