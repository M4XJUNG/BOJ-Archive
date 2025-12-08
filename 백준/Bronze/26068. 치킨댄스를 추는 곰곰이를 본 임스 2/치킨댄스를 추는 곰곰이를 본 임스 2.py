# 26068 치킨댄스를 추는 곰곰이를 본 임스 2
n = int(input())
count = 0
for i in range(n):
  x = input()
  c = int(x[2:])
  if c <= 90: count += 1
print(count)