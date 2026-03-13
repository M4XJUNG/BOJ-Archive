# 3733_Shares
import sys

# 1. 파일의 끝(EOF)까지 모든 입력을 하나의 거대한 문자열로 통째로 읽어옵니다.
# 2. sys.stdin.read()까지만 하게 되면 data = "1 100\n2\n7\n\n10   9"로 저장됨. 
# 3. .split()을 쓰면 띄어쓰기(공백)와 엔터(\n)를 전부 무시하고 깔끔하게 쪼개서 리스트에 담아줍니다.
# 4. data = ['1', '100', '2', '7', '10', '9', '10', '10'] 이렇게 들어감. 
data = sys.stdin.read().split()

# 이제 data 리스트 안에는 모든 입력값이 순서대로 예쁘게 들어있습니다.
# (예: 데이터를 2개씩 짝지어서 처리해야 하는 경우)
for i in range(0, len(data), 2):
    A = int(data[i])
    B = int(data[i+1])
    print(B // (A + 1))