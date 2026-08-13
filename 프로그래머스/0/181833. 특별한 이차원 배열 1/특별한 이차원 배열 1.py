import numpy as np
def solution(n):
    answer = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
    return answer.tolist()