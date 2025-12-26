# 30868 개표
T = int(input())
for _ in range(T):
  n = int(input())
  plus_part = "++++ " * (n // 5)
  stick_part = "|" * (n % 5)
  print(plus_part + stick_part)