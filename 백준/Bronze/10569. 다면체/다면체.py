# 10569 다면체
n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  print(b - a + 2)