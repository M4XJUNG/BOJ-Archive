def solution(numLog):
    wasd = {
        1: 'w',
        -1: 's', 
        10: 'd', 
        -10: 'a'
    }
    answer = ''
    for i in range(len(numLog) - 1):
        change = numLog[i + 1] - numLog[i]
        answer += wasd[change]
    return answer