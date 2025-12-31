# 31495 그게 무슨 코드니.. 2026-01-01(목) 오전 8:35
# import sys
# input = sys.stdin.readline 
S = input()
if len(S) > 2 and S[0] == '"' and S[-1] == '"': print(S[1:-1])
else: print('CE')