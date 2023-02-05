N = int(input())

def func(x):
    return x ** 3 + x

L = 1.0
R = 100.0
while R - L > 0.0001:
    M = (L + R) / 2
    if func(M) <= N:
        L = M
    if func(M) > N:
        R = M

print(M)