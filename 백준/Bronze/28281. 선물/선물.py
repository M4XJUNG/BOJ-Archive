# 28281_선물 
N, X = map(int, input().split())
N_lst = list(map(int, input().split()))
cnt = N_lst[0] + N_lst[1]
for i in range(N - 1):
    if N_lst[i] + N_lst[i+1] < cnt: 
        cnt = N_lst[i] + N_lst[i+1]
print(cnt * X)