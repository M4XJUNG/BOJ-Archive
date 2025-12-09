# 25640 MBTI
mbti = input()
n = int(input())
count = 0
for i in range(n):
  friend_mbti = input()
  if mbti == friend_mbti: count += 1
print(count)