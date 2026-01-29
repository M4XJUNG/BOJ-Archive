# 34750 추석은 언제나 좋아 2026-01-30(금) 오전 7:58
import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
if 1000000 <= N: cnt = N * 0.2
elif 500000 <= N < 1000000: cnt = N * 0.15
elif 100000 <= N < 500000: cnt = N * 0.1
else: cnt = N * 0.05
print(int(cnt), int(N - cnt))