# 2920번 음계 - 10월 31일 (금)
numbers = list(map(int, input().split()))
ascending_count = 0
descending_count = 0
for i in range(8):
  if numbers[i] == i + 1: ascending_count += 1
  elif numbers[i] == (8 - i): descending_count += 1
if ascending_count == 8: print("ascending")
elif descending_count == 8: print("descending")
else: print("mixed")