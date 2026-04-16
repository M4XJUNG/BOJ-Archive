# 25591 푸앙이와 종윤이
n, m = map(int, input().split())
a = 100 - n
b = 100 - m
c = 100 - a - b
d = a * b
q = a * b // 100
r = a * b % 100
print(a, b, c, d, q, r)
print(c + q, r)