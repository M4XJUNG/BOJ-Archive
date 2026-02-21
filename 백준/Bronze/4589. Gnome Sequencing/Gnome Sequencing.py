# 4589 Gnome Sequencing
print("Gnomes:")
n = int(input())
for i in range(n):
  a, b, c = map(int, input().split())
  if a <= b <= c or a >= b >= c: print("Ordered")
  else: print("Unordered")