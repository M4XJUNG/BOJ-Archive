# 15726 이칙연산 2026-02-03(화) 오전 2:50
A, B, C = map(int, input().split())
mul_div = A * B / C
div_mul = A / B * C
print(int(max(mul_div, div_mul)))