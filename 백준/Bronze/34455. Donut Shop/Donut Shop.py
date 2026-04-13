# 34455_Donut Shop
d = int(input())
e = int(input())
for _ in range(e):
    s = input()
    q = int(input())
    if s == '+': d += q 
    elif s == '-': d -= q 
print(d)