def solution(age):
    answer = []
    age_change = {
        0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 
        5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j'
    }
    for _ in range(len(str(age))):
        answer.append(age_change[age % 10])
        age = age // 10 
    return ''.join(answer[::-1])
    ''' 사실 숫자를 문자로 바꾸는 문제는 translate가 제일 많이 쓰인다.
    table = str.maketrans(
        "0123456789", 
        "abcdefghij"
    )
    return str(age).translate(table)
    '''