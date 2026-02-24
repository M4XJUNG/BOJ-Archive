# 25377_빵
N = int(input())
cant_buy = 0
can_buy = 1000
for _ in range(N):
    A, B = map(int, input().split())
    if A > B: cant_buy += 1
    else: 
        if can_buy > B: can_buy = B

if cant_buy == N: print(-1)
else: print(can_buy)