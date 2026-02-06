# 19698 헛간 청약 2026-02-07(금) 오전 10:49
import sys
input = sys.stdin.readline
N, W, H, L = map(int, input().split())
capacity = (W // L) * (H // L)
print(min(N, capacity))