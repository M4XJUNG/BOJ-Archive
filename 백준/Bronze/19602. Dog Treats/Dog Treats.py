# 19602_Dog Treats
S = int(input())
M = int(input())
L = int(input())
cnt = S + M * 2 + L * 3
if cnt >= 10:
    print('happy')
else:
    print('sad')