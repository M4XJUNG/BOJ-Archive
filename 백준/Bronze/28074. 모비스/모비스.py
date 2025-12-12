# 28074 모비스
st = input()
m_count = o_count = b_count = i_count = s_count = 0
for i in range(len(st)):
  if st[i] == 'M': m_count += 1
  elif st[i] == 'O': o_count += 1
  elif st[i] == 'B': b_count += 1
  elif st[i] == 'I': i_count += 1
  elif st[i] == 'S': s_count += 1
judge = m_count and o_count and b_count and i_count and s_count 
if judge: print("YES")
else: print("NO")