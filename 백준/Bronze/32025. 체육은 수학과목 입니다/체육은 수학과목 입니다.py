# 32025 체육은 수학과목 입니다 2026-01-10(토) 오전 1:57
import sys
input = sys.stdin.readline
H = int(input())
W = int(input())
print(int((H / 2) * 100) if H < W else int((W / 2) * 100))