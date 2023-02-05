N = int(input())

# 整数xが消されているときDel[x]=True
Del = [False] * 1000009
LIMIT = int(N**0.5)
for i in range(2, LIMIT+1):
    if Del[i] == False:
        for j in range(i*2, N+1, i):
            Del[j] = True

for i in range(2, N+1):
	if Del[i] == False:
		print(i)