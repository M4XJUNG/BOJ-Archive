# 31090 2023은 무엇이 특별할까?
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  N = int(input())
  if (N + 1) % (N % 100) == 0: print('Good')
  else: print('Bye')