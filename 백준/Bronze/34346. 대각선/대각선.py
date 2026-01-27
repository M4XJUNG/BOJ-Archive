# 34346 대각선 2026-01-27(화) 오후 5:38
import sys
input = sys.stdin.readline
N = int(input())
# N이 홀수면(교차점이 있음) -> 1칸 (가운데)
if N % 2 == 1: print(1)
# N이 짝수면(교차점이 없음) -> 2칸 (양쪽 각각)
else: print(2)