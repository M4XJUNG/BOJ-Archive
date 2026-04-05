def solution(n):
    answer = 0
    if n % 7 == 0: answer = n // 7
    else: answer = n // 7 + 1
    return answer

'''
1~7 = 1
8~14 = 2
15~21 = 3
n // 7 + 1
if n % 7 == 0: answer = n // 7
else: answer = n // 7 + 1
'''