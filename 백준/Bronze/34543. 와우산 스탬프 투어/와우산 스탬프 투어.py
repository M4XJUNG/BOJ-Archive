# 34543 와우산 스탬프 투어 2026-01-29(목) 오전 12:08
import sys
input = sys.stdin.readline
N = int(input())
W = int(input())
place = { 0 : 0, 1 : 10, 2 : 20, 3 : 50, 4 : 60, 5 : 120 }
if W <= 1000: print(place[N])
elif place[N] < 15: print(0)
else: print(place[N] - 15)