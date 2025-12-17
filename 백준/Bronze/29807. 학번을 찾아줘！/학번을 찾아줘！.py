# 29807 학번을 찾아줘!
n = int(input())
score = list(map(int, input().split()))
while len(score) < 5: score.append(0)
count = 0
if score[0] > score[2]: count += (score[0] - score[2]) * 508
else: count += (score[2] - score[0]) * 108
if score[1] > score[3]: count += (score[1] - score[3]) * 212
else: count += (score[3] - score[1]) * 305
if score[4] != 0: count += score[4] * 707
count *= 4763
print(count)