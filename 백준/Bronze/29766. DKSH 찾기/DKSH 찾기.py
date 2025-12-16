# 29766 DKSH 찾기
DKSH = 'DKSH'
s = input()
count = 0
for i in range(3, len(s)):
  if s[i-3] == 'D' and s[i-2] == 'K' and s[i-1] == 'S' and s[i] == 'H':
    count += 1
print(count)