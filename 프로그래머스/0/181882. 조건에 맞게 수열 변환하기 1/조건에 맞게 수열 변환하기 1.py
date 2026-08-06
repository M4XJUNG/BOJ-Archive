def solution(arr):
    answer = []
    for num in arr:
        if num < 50 and num % 2 != 0:
            answer.append(num * 2)
        elif num >= 50 and num % 2 == 0:
            answer.append(num / 2)
        else:
            answer.append(num)
    return answer
    # 오류가 난다면, num // 2로 바꿔보기
    # 개선점 
    # 1. num % 2 만 해줘도 됨. 