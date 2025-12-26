# 1264 모음의 개수
while True:
  count = 0
  sen = input()
  if sen == '#': break
  for i in sen:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
      count += 1
  print(count)