import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))

index = bisect.bisect_left(A, X)
print(index+1)