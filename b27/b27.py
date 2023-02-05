A, B = map(int, input().split())

def gcd(x, y):
    n = max(x, y)
    m = min(x, y)
    while m != 0:
        amari = n % m
        n = m
        m = amari
    return n

Answer = A * B // gcd(A, B)
print(Answer)