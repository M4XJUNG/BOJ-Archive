# 32369 양파 실험 2026-01-14(수) 오전 3:17
import sys
input = sys.stdin.readline
a, b = 1, 1
N, A, B = map(int, input().split())
for _ in range(N):
	a += A
	b += B
	if a == b: b -= 1
	if a < b: a, b = b, a
print(a, b)