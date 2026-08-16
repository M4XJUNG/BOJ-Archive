def solution(a, d, included):
    # 3 7 11 15 19 -> 3 + 15 + 19 = 37
    # 7 8 9 10 11 12 13 -> 10
    
    # add_num = []
    # result = 0
    # for i in range(len(included)):
    #     add_num.append(a + (d * i))
    # for a, ic in zip(add_num, included):
    #     if ic: 
    #         result += a
    # return result 
    
    # answer = 0
    # for i, bool in enumerate(included):
    #     if bool:
    #         answer += a + d * i
    # return answer 
    return sum(
        a + d * i 
        for i, include in enumerate(included) 
        if include 
    )