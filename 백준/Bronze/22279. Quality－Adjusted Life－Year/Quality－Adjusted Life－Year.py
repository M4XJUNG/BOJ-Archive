# 22279_Quality-Adjusted Life-Year 
n = int(input())
cnt = 0
for _ in range(n):
    q, y = map(float, input().split())
    cnt += (q * y)
print(f'{cnt:.3f}')