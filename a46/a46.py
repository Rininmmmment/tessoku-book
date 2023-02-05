# (x, y)

N = int(input())
X, Y = [None] * (N-1), [None] * (N-1)
for i in range(N-1):
    X[i], Y[i] = map(int, input().split())

class point2d:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	# 2 点間の距離を求める関数
	def dist(self, p):
		return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

print(point2d(X[0], Y[0]).dist(point2d(X[1], Y[1])))