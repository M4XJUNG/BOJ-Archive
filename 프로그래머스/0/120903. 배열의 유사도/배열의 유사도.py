def solution(s1, s2):
    count = len(set(s1) & set(s2))
    return count