# 30008 준영이의 등급
n, k = map(int, input().split())
num = list(map(int, input().split()))
p = []
for i in range(k):
  p.append(num[i] * 100 // n)
  if 0 <= p[i] <= 4: p[i] = 1
  elif 4 < p[i] <= 11: p[i] = 2
  elif 11 < p[i] <= 23: p[i] = 3
  elif 23 < p[i] <= 40: p[i] = 4
  elif 40 < p[i] <= 60: p[i] = 5
  elif 60 < p[i] <= 77: p[i] = 6
  elif 77 < p[i] <= 89: p[i] = 7
  elif 89 < p[i] <= 96: p[i] = 8
  elif 96 < p[i] <= 100: p[i] = 9
print(*p)