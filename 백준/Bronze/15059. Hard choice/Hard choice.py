# 15059_Hard choice
C_a, B_a, P_a = map(int, input().split())
C_r, B_r, P_r = map(int, input().split())

total = 0
if C_a < C_r:
    total += C_r - C_a
if B_a < B_r:
    total += B_r - B_a
if P_a < P_r:
    total += P_r - P_a

print(total)