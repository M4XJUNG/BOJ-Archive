# 18408_3 つの整数 (Three Integers)
num = list(map(int, input().split()))
if num.count(1) > num.count(2): print(1)
elif num.count(1) < num.count(2): print(2)