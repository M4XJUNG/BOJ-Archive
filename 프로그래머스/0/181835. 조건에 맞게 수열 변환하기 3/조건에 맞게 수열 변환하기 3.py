import numpy as np
def solution(arr, k):
    arr = np.array(arr)
    return (arr + k).tolist() if k % 2 == 0 else (arr * k).tolist()