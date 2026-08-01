def solution(my_string, is_suffix):
    # in_my_string = []
    # for i in range(len(my_string)):
    #     in_my_string.append(my_string[i:])
    # if is_suffix in in_my_string:
    #     return 1 
    # else: return 0
    return 1 if is_suffix in [my_string[i:] for i in range(len(my_string))] else 0 