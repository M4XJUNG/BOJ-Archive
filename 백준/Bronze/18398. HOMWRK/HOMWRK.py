# 18398_HOMWRK
T = int(input())
for _ in range(T):
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        print(f'{A + B} {A * B}')