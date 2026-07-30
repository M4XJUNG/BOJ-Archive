def solution(my_string):
    # result = []
    # for i in range(len(my_string)):
    #     result.append(my_string[i:])
    return sorted(my_string[i:] for i in range(len(my_string)))
    
    # Case 2에서 모든 접미사를 구하고 나서 사전순으로 정렬해야함. 