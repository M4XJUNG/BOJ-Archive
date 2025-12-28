# 30999 민주주의
N, M = map(int, input().split())
cnt = 0
for _ in range(N):
  s = input()
  if s.count('O') > s.count('X'): cnt += 1
print(cnt)