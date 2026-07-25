def solution(arr, idx):
    # arr[idx] ~ arr[-1] 1이 있으면 인덱스 반환, 1 없으면 -1 반환
    for i in range(idx, len(arr)):
        if arr[i] == 1: return i
    return -1