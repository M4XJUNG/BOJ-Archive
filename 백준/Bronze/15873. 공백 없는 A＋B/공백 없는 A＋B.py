# 15873 공백 없는 A+B
n = int(input())
if n % 100 == 10: print(n // 100 + n % 100)
else: print(n // 10 + n % 10)