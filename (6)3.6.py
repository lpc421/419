n = 3  

for i in range(1, n + 2):
    print(' ' * (n + 1 - i) + '*' * (2 * i - 1))

for i in range(n, 0, -1):
    print(' ' * (n + 1 - i) + '*' * (2 * i - 1))