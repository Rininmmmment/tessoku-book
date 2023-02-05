# 答えがmidだとしたとき、合計枚数はK枚になるかどうか
def check(mid, A, N):
    sum = 0
    for i in range(N):
        sum += mid // A[i]
    return sum

N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10 ** 9

while l < r:
    mid = (l+r) // 2
    if check(mid, A, N) >= K:
        r = mid
    else:
        l = mid+1
print(l)