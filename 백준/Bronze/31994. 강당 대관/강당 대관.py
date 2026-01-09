# 31994 강당 대관 2026-01-09(금) 오후 3:42
import sys
input = sys.stdin.readline

semina = {}  # 빈 딕셔너리 생성

for _ in range(7):
    # 1. 입력받고 쪼개기 (언패킹)
    line = input().split() 
    name = line[0]        # 학회 이름
    count = int(line[1])  # 사람 수 (꼭 int로 변환!)

    # 2. 딕셔너리에 넣기: semina[키] = 값
    semina[name] = count 

# 3. 최댓값 찾기 (이게 좀 마법 같은 문법입니다)
# max(딕셔너리, key=딕셔너리.get) -> 값(value)을 기준으로 키(key)를 내놔라
result = max(semina, key=semina.get)
print(result)