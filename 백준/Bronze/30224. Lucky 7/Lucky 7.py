n = int(input())
str_n = str(n)

# n이 문자열로 '7'을 포함하는지 여부
has_seven = "7" in str_n
# n이 7로 나누어 떨어지는지 여부
is_divisible_by_seven = (n % 7 == 0)

# 두 조건의 조합에 따라 결과 출력
if has_seven and is_divisible_by_seven:
    print(3)
elif has_seven and not is_divisible_by_seven:
    print(2)
elif not has_seven and is_divisible_by_seven:
    print(1)
else:
    print(0)