def solution(a, b):
    a_b = int(str(a) + str(b))
    b_a = int(str(b) + str(a))
    if a_b >= b_a: answer = a_b
    else: answer = b_a
    return answer