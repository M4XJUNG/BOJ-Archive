# 5928_Contest Timing
D, H, M = map(int, input().split())
total_minutes = (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)
if total_minutes < 0: print(-1)
else: print(total_minutes)