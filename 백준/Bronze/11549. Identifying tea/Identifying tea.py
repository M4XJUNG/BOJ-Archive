# 11549_Identifying tea
T = int(input())
cnt = 0 
contestants = list(map(int, input().split()))
for guess in contestants:
    if T == guess: cnt += 1
print(cnt)