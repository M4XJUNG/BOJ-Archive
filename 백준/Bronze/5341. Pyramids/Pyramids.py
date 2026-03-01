def pyramid(n):
  if n == 0: return 0
  return n + pyramid(n - 1)
while True:
  n = int(input())
  if n == 0: break
  print(pyramid(n))