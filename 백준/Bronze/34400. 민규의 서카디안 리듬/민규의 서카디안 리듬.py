# 34400 민규의 서카디안 리듬 2026-01-28(수) 오전 2:02
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  t = int(input())
  if t % 25 <= 16: print('ONLINE')
  else: print('OFFLINE')