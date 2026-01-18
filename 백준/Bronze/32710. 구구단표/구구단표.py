# 32710 구구단표 2026-01-18(일) 오후 2:16
import sys
input = sys.stdin.readline
N = int(input())
table = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 48, 45, 49, 54, 56, 63, 64, 72, 81]
if N in table: print(1)
else: print(0)