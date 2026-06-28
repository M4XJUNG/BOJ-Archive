def solution(num_list):
    e_n = o_n = ''
    for num in num_list:
        if num % 2 == 0:
            e_n += str(num)
        else: 
            o_n += str(num)
    return int(e_n) + int(o_n)