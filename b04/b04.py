N = input()

Answer = 0
len = int(len(N))
for i in range(len):
    Answer += int(N[len-i-1]) * (2 ** i)

print(Answer)