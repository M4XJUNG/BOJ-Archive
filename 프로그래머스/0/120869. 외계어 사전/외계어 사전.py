def solution(spell, dic):
    words = ''.join(spell)
    for word in dic:
        if sorted(words) == sorted(word):
            return 1
    return 2