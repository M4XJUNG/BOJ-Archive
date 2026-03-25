# 23235_The Fastest Sorting Algorithm In The World
case_num = 1

while True:
    # 한 줄의 입력을 받아 리스트로 변환합니다.
    data = list(map(int, input().split()))
    
    # 첫 번째 숫자가 0이면 종료합니다.
    if data[0] == 0: break
        
    # 입력된 배열의 내용은 무시하고 정해진 문구만 출력합니다.
    print(f"Case {case_num}: Sorting... done!")
    case_num += 1