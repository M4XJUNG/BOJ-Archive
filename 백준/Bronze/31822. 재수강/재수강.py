# 31822 재수강 2026-01-05(월) 오전 02:45
import sys
input = sys.stdin.readline
code = input()
N = int(input())
count = 0
for _ in range(N):
  input_code = input()
  if code[:5] == input_code[:5]: count += 1
print(count)