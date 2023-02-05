def Power(a, b, m):    # a^b % m を計算
	p = a
	Answer = 1
	for i in range(30):
		wari = 2 ** i
		if (b // wari) % 2 == 1:
			Answer = (Answer * p) % m
		p = (p * p) % m
	return Answer

n, r = map(int, input().split())
M = 1000000007

# 分母をMで割ったあまり
a = 1
for i in range(1, n+1):
    a = (a * i) % M

# 分子をMで割ったあまり
b = 1
for i in range(1, r+1):
    b = (b * i) % M
for i in range(1, n-r+1):
    b = (b * i) % M

# 答えを求める
c = Power(b, M-2, M)
Answer = (a * c) % M
print(Answer)