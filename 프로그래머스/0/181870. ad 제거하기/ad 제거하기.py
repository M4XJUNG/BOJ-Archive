def solution(strArr):
    answer = []
    for str in strArr:
        if 'ad' in str: 
            continue
        else: 
            answer.append(str)
    return answer 