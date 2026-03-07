# 27918_탁구 경기
N = int(input())
d_win = p_win = 0
for _ in range(N):
    vic = input() 
    if abs(d_win - p_win) < 2:
        if vic == 'D':
            d_win += 1
        else:
            p_win += 1
print(f'{d_win}:{p_win}')
