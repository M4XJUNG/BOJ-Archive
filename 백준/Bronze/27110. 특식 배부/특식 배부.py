# 27110 특식 배부
n = int(input())
a, b, c = map(int, input().split())
count = 0
if n >= a: count += a
else: count += n  
if n >= b: count += b
else: count += n 
if n >= c: count += c
else: count += n 
print(count)