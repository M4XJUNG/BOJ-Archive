# 14470 전자레인지
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
if a < 0: count = a * -1 * c + d + b * e
elif a > 0: count = (b - a) * e
print(count)