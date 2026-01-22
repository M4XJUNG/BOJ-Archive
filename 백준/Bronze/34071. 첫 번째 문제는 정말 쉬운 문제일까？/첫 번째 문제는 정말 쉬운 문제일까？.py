# 34071 첫 번째 문제는 정말 쉬운 문제일까? 2026-01-23(금) 오전 4:28
import sys
input = sys.stdin.readline
N = int(input())
level = [ int(input()) for _ in range(N) ]
if min(level) == level[0]: print('ez')
elif max(level) == level[0]: print('hard')
else: print('?')