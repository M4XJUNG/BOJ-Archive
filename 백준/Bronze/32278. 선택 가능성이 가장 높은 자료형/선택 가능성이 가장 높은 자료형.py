# 32278 선택 가능성이 가장 높은 자료형 2026-01-12(월) 오전 4:13
import sys
input = sys.stdin.readline
N = int(input())
if -32768 <= N <= 32767: print('short')
elif -2147483648 <= N <= 2147483647: print('int')
else: print('long long')