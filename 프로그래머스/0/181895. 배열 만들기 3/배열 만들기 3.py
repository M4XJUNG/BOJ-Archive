def solution(arr, intervals):
    # a1, b1 = intervals[0]
    # a2, b2 = intervals[1]
    # or 
    # (a1, b1), (a2, b2) = intervals
    # return arr[a1:b1+1] + arr[a2:b2+1]
    # or
    # for a, b in intervals:
    #   answers += arr[a:b+1]
    return arr[intervals[0][0]:intervals[0][1] + 1] + arr[intervals[1][0]:intervals[1][1] + 1]