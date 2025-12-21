# 30031 지폐 세기
n = int(input())
count = 0
for i in range(n):
  width, length = map(int, input().split())
  if width == 136: count += 1000
  elif width == 142: count += 5000
  elif width == 148: count += 10000
  elif width == 154: count += 50000
print(count)