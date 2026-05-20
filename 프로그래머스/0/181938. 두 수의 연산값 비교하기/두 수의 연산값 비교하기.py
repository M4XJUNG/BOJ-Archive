def solution(a, b):
    answer = 0
    c_p = int(str(a) + str(b))
    multi = 2 * a * b
    if c_p >= multi: answer = c_p
    else: answer = multi
    return answer