# 32684 장기 2026-01-17(토) 오후 2:57
import sys
input = sys.stdin.readline

# 1. 점수표를 리스트로 선언 (차, 포, 마, 상, 사, 졸 순서)
# 딕셔너리({})도 좋지만, 입력 데이터가 순서대로 들어오기 때문에 점수판도 리스트([])로 만드는 게 인덱스(i) 맞추기가 훨씬 편합니다.
scores = [13, 7, 5, 3, 3, 2]

# 2. 입력 받기
cjr = list(map(int, input().split())) # 초나라 (cocjr0208)
dms = list(map(int, input().split())) # 한나라 (ekwoo)

# 3. 점수 계산을 위한 변수 초기화
cjr_score = 0
dms_score = 1.5 # [중요] 한나라는 1.5점 덤을 받고 시작!

# 4. 반복문으로 곱해서 더하기
for i in range(6):
    # (내 기물 개수) * (해당 기물의 점수)
    cjr_score += cjr[i] * scores[i]
    dms_score += dms[i] * scores[i]

# 5. 비교 및 출력
if cjr_score > dms_score: print('cocjr0208')
else: print('ekwoo')