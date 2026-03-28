# 5300_Fill the Rowboats!
N = int(input())
for i in range(1, N + 1):
    print(i, sep = ' ', end = ' ')
    if i % 6 == 0 or i == N:
        print('Go!', sep = ' ', end = ' ')