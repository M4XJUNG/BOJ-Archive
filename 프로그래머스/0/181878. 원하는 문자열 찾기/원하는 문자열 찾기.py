def solution(myString, pat):
    return 1 if myString.lower().find(pat.lower()) >= 0 else 0