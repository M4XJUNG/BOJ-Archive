def solution(myString):
    return sorted(myString.replace('x', ' ').split())
# return sorted(s for s in myString.split('x') if s)