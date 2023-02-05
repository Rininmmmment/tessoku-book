N = int(input())

for i in reversed(range(10)):
    wari = N // (2 ** i)
    print(wari % 2, end='')
print('')