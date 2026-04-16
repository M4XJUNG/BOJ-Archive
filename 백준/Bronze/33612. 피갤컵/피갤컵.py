# 33612 피갤컵
n = int(input())
y = 2024
m = 8
y = y + n * 7 // 12
m = (m + ((n - 1) * 7)) % 12
if m == 0: print(y, 12)
else: print(y, m)