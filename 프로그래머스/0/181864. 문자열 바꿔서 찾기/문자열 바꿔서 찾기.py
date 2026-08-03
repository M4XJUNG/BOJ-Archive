def solution(myString, pat):
    change = {
        'A': 'B', 
        'B': 'A'
    }
    return 1 if pat in "".join(change[ch] for ch in myString) else 0