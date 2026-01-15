# 32642 당구 좀 치자 제발 2026-01-15(목) 오후 1:21
import sys
input = sys.stdin.readline
N = int(input())
rain = input().split()
cnt = total = 0
for i in range(N):
  if int(rain[i]) == 1: cnt += 1
  else: cnt -= 1
  total += cnt 
print(total)