# 時間xまでに何枚印刷されているか
def check(x, N, K, A):
	sum = 0
	for i in range(N):
		sum += x // A[i] # 「x÷A[i]」の小数点以下切り捨て

	if sum >= K:
		return True
	return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = 10 ** 9
while L < R:
    M = (L + R) // 2
    answer = check(M, N, K, A)
    if answer == True:
        R = M
    if answer == False:
        L = M + 1

print(L)