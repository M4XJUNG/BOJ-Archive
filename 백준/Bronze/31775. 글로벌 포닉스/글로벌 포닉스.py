# 31775 글로벌 포닉스 2026-01-03(토) 오전 4:30
s1 = input()
s2 = input()
s3 = input()

# 1. 첫 글자만 따서 리스트 만들기
first_chars = [s1[0], s2[0], s3[0]]

# 2. 정렬해버리기 (k, l, p 순서로 예쁘게 줄 세움)
first_chars.sort()

# 3. 정답이랑 비교
if first_chars == ['k', 'l', 'p']: print("GLOBAL")
else: print("PONIX")