def func(x):
    return x ** 3 + x

N = int(input())

r = 100
l = 0

while r - l > 0.0001:
    mid = (l+r) / 2
    if func(mid) <= N:
        l = mid
    else:
        r = mid
print(mid)