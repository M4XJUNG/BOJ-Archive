import sys
input = sys.stdin.readline

N = int(input())
K = input().strip()  # 숫자가 아니라 '문자열'로 받습니다! (중요)

even_count = 0
odd_count = 0

for digit in K:
    # 문자 하나를 숫자로 바꿔서 짝홀 판별
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print(0)
elif even_count < odd_count:
    print(1)
else:
    print(-1)