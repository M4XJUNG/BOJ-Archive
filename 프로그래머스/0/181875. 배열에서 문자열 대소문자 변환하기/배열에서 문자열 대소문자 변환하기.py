def solution(strArr):
    # return [word.lower() if i % 2 == 0 else word.upper() for i, word in enumerate(strArr)] 
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0: answer.append(strArr[i].lower())
        else: answer.append(strArr[i].upper())
    return answer