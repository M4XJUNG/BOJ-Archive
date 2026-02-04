import sys
input = sys.stdin.readline

x = input().strip()

while True:
    # 1. 먼저 값을 계산합니다. (사용자님의 로직 그대로!)
    # 첫째 자리 * 길이
    val = int(x[0]) * len(x)
    
    # 2. 계산된 값을 문자열로 바꿉니다. (다음 턴을 위해)
    next_x = str(val)
    
    # 3. [핵심] 멈추는 조건
    # 계산했는데 값이 안 변했으면 'FA수'가 된 것입니다.
    if next_x == x:
        print("FA")
        break
    
    # 4. 값이 다르면 x를 갱신하고 계속 돕니다.
    x = next_x