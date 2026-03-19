# 28097_모범생 포닉스
N = int(input())
T = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += T[i]
cnt += (N-1) * 8
h_cnt = cnt // 24 
m_cnt = cnt % 24
print(h_cnt, m_cnt)