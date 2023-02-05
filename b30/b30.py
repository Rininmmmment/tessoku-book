H, W = map(int, input().split())
M = 1000000007

def Power(a, b, m):    # a^b % m を計算
	p = a
	Answer = 1
	for i in range(30):
		wari = 2 ** i
		if (b // wari) % 2 == 1:
			Answer = (Answer * p) % m
		p = (p * p) % m
	return Answer

# 分母 % M
a = 1
for i in range(1, H+W-1):
    a = (a * i) % M

# 分子 % M
b = 1
for i in range(1, H):
    b = (b * i) % M
for i in range(1, W):
    b = (b * i) % M

# 答え
c = Power(b, M-2, M)
Answer = (a * c) % M
print(Answer)