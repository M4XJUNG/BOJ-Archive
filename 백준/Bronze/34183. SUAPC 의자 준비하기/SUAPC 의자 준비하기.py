# 34183 SUAPC 의자 준비하기 2026-01-24(토) 오후 4:58
N, M, A, B = map(int, input().split())
if 3 * N <= M: print(0)
else: print((3 * N - M) * A + B)