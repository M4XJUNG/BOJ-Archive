# 31962 등교 2026-01-08(목) 오전 3:47
import sys
input = sys.stdin.readline
N, X = map(int, input().split())
time_cnt = []
for _ in range(N):
  S, T = map(int, input().split())
  if S + T > X: continue
  else: time_cnt.append(S)
time_cnt.sort()
if time_cnt == []: print(-1)
else: print(time_cnt[-1])