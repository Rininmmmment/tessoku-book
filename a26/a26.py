def isPrime(N):
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT+1):
        if N % i == 0:
            return False
    return True

# ε₯ε
Q = int(input())
X = [ None ] * Q
for i in range(Q):
	X[i] = int(input())

# εΊε
for i in range(Q):
    if isPrime(X[i]) == True:
        print('Yes')
    else:
        print('No')