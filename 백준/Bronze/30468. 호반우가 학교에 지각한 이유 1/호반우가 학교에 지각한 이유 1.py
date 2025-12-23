# 30468 호반우가 학교에 지각한 이유 1
import sys
input = sys.stdin.readline

STR, DEX, INT, LUK, N = map(int, input().split())
TOT = (STR + DEX + INT + LUK)
if N * 4 > TOT: print(N * 4 - TOT)
else: print(0)