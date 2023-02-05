N = int(input())
p, q, r = 3, 5, 7

Answer = 0
P = N // p
Q = N // q
R = N // r
PQ = N // (p * q)
QR = N // (q * r)
RP = N // (r * p)
PQR = N // (p * q * r)

Answer = P + Q + R - PQ - QR - RP + PQR
print(Answer)