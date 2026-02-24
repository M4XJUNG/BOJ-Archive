# 25494_단순한 문제 (Small)
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    print(min(a, b, c))
