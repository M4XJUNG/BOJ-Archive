# 34323 할인이 필요해 2026-01-26(월) 오전 11;57
N, M, S = map(int, input().split())
discount_N = int(round((1 - (N / 100)) * (M + 1) * S, 5))
discount_M = M * S
print(discount_N if discount_N < discount_M else discount_M)