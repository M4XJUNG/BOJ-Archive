# 32651 인간은 무엇인가 2026-01-16(금) 오전 11:40
import sys
input = sys.stdin.readline
N = int(input())
if N <= 100000 and N % 2024 == 0: print('Yes')
else: print('No')