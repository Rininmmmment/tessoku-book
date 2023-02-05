A, B = map(int, input().split())

n = max(A, B)
m = min(A, B)

while m != 0:
    amari = n % m
    n = m
    m = amari
    # print(n, m)
print(n)
    