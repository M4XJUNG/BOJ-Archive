def solution(str1, str2):
    return ''.join(f'{a}{b}' for a, b in zip(str1, str2))