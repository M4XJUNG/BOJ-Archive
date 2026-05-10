def solution(n):
    result = 0
    for i in range(1, 1001):
        if i ** 2 == n: 
            result = 1 
            break
        else: result = 2
    return result