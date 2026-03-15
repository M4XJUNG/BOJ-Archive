# 27434_팩토리얼 3
N = int(input())
result = 1
for i in range(N, 0, -1):
    result *= i 
print(result)