# 34236 숭고한에 어서오세요 2026-01-25(일) 오전 1:14
import sys
input = sys.stdin.readline
N = int(input())
years = list(map(int, input().split()))
print(years[-1] + years[1] - years[0])