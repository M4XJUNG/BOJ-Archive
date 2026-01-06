# 31922 이 대회는 이제 제 겁니다 2026-01-07(수) 오전 2:12
import sys
input = sys.stdin.readline
A, P, C = map(int, input().split())
if A + C > P: print(A + C)
else: print(P)