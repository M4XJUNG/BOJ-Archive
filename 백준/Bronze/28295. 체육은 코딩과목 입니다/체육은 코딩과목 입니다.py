# 28295 체육은 코딩과목 입니다
dirs = "NESW"
delta = [0, 1, 2, -1]  # n=1,2,3에 대응 (0은 더미)

idx = 0  # N
for _ in range(10):
    n = int(input())
    idx = (idx + delta[n]) % 4

print(dirs[idx])
