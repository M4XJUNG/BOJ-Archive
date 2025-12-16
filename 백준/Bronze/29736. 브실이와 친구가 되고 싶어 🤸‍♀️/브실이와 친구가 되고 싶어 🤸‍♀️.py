# 29736 브실이와 친구가 되고 싶어 🤸‍♀️
a, b = map(int, input().split())
result1 = [i for i in range(a, b + 1)]
result2 = []
count = 0
k, x = map(int, input().split())
for j in range(k - x, k + x + 1):
  if j in result1:
    count += 1
if count == 0: print("IMPOSSIBLE")
else: print(count)