def Power(a, b, m):    # a^b % m を計算
	p = a
	Answer = 1
	for i in range(30):
		wari = 2 ** i
		if (b // wari) % 2 == 1:
			Answer = (Answer * p) % m
		p = (p * p) % m
	return Answer

# 入力
a, b = map(int, input().split())

# 出力
print(Power(a, b, 1000000007))