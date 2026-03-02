# 28431_양말 짝 맞추기
num = [] 
for _ in range(5):
    num.append(int(input()))
for sock in num:
    if num.count(sock) % 2 != 0: 
        print(sock)
        break