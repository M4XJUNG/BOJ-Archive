def solution(num_list):
    answer = sorted(num_list)
    for i in range(5):
        answer.pop(0)
    return answer