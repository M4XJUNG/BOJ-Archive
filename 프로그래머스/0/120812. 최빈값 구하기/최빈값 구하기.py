from collections import Counter
def solution(array):
    counter = Counter(array)
    common = counter.most_common()
    if len(common) >= 2 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]: return -1
    else: return counter.most_common(1)[0][0]

# counter = Counter(data)

# 최빈값과 빈도를 튜플 형태로 모두 출력
# print(counter.most_common()) 
# 출력: [(3, 3), (2, 2), (1, 1), (4, 1)]

# 가장 빈도가 높은 최빈값의 숫자만 출력
# mode_value = counter.most_common(1)[0][0]
# print(mode_value) 
# 출력: 3
