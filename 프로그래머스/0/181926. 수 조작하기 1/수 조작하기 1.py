def solution(n, control):
    answer = n
    wsda = {'w':1, 's':-1, 'd':10, 'a':-10}
    for c in control:
        answer += wsda[c]
    return answer