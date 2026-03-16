# 25704_출석 이벤트
N = int(input())
P = int(input())
cnt = P
if N >= 20: cnt = min(P * 0.75, P - 2000)
elif N >= 15: cnt = min(P - 2000, P * 0.9)
elif N >= 10: cnt = min(P * 0.9, P - 500)
elif N >= 5: cnt = P - 500
if cnt >= 0: print(int(cnt))
else: print(0)