# 27890 특별한 작은 분수
x, n = map(int, input().split())
count = 0
for _ in range(n):
  if x % 2 == 0: 
    count = x // 2 ^ 6
    x = count 
  else: 
    count = x * 2 ^ 6
    x = count 
print(x)