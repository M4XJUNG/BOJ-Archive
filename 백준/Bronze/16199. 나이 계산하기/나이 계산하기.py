# 16199_나이 계산하기
import sys
input = sys.stdin.readline

# 1. 입력 받기
b_y, b_m, b_d = map(int, input().split()) # 태어난 날짜
c_y, c_m, c_d = map(int, input().split()) # 기준 날짜

# 2. 만 나이 계산 (핵심)
# 일단 연도 차이를 구함
man_age = c_y - b_y

# 아직 생일이 안 지났다면 1살을 더 뺌
if c_m < b_m: # 기준 월이 생일 월보다 전일 때
    man_age -= 1
elif c_m == b_m: # 같은 달인데
    if c_d < b_d: # 기준 일이 생일 일보다 전일 때
        man_age -= 1

# 3. 세는 나이 & 연 나이 계산
korean_age = c_y - b_y + 1
year_age = c_y - b_y

# 4. 출력
print(man_age)
print(korean_age)
print(year_age)