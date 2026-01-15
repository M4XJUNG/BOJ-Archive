import sys
input = sys.stdin.readline

N = int(input())
# map으로 미리 숫자로 다 바꿔둡니다. (반복문 안에서 int() 호출 비용 절약)
rain = list(map(int, input().split()))

cnt = 0
total_anger = 0  # [수정] sum 대신 충돌 안 나는 이름 사용

for x in rain:
    # [최적화] if문 삭제 -> 수학적 매핑 (1 -> 1, 0 -> -1)
    cnt += (x * 2 - 1) 
    total_anger += cnt

print(total_anger)