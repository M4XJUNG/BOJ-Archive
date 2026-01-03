# 31821 학식 사주기 2026-01-04(일) 오전 06:50
import sys
input = sys.stdin.readline
N = int(input())
menu = [int(input()) for _ in range(N)]
M = int(input())
count = 0
for _ in range(M):
  want = int(input())
  count += menu[want - 1]
print(count)