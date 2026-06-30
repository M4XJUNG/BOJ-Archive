def solution(my_string, target):
    return 1 if target in my_string else 0 
# 삼항 연산자조차 필요 없다! 그냥 논리 결과(True/False)를 숫자로 바꿔라!
# return int(target in my_string)