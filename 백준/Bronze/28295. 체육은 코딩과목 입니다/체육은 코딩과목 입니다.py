# 28295 체육은 코딩과목 입니다
dir = 'N'
for i in range(10):
  n = int(input())
  if n == 1:
    if dir == 'N': dir = 'E'
    elif dir == 'E': dir = 'S'
    elif dir == 'S': dir = 'W'
    elif dir == 'W': dir = 'N'
  elif n == 2:
    if dir == 'N': dir = 'S'
    elif dir == 'E': dir = 'W'
    elif dir == 'S': dir = 'N'
    elif dir == 'W': dir = 'E'
  elif n == 3:
    if dir == 'N': dir = 'W'
    elif dir == 'E': dir = 'N'
    elif dir == 'S': dir = 'E'
    elif dir == 'W': dir = 'S'
print(dir)