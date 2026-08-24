def solution(arr):
    n = len(arr)

    for i in range(11):
        if 2 ** i >= n:
            arr += [0] * (2 ** i - n)
            break

    return arr