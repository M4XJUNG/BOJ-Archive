# 350927_2025
while True:
    n = int(input())
    cnt = 0
    if n == 0: break 
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cnt += (i * j)
    print(cnt)