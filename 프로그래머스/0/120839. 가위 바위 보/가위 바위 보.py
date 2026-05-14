def solution(rsp):
    answer = []
    result = {'2':'0', '0':'5', '5':'2'}
    for i in range(len(rsp)):
        answer.append(result.get(rsp[i]))
    return ''.join(answer)