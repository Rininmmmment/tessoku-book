N = int(input())
p, q = 3, 5

Answer = 0
P_count = N // p
Q_count = N // q
PQ_count = N // (p * q)

Answer = P_count + Q_count - PQ_count
print(Answer)