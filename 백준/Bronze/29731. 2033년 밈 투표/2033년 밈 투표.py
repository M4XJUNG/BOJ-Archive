# 29731_2033년 밈 투표
import sys
input = sys.stdin.readline
promise = [
    'Never gonna give you up', 
    'Never gonna let you down', 
    'Never gonna run around and desert you', 
    'Never gonna make you cry', 
    'Never gonna say goodbye', 
    'Never gonna tell a lie and hurt you', 
    'Never gonna stop'
]
N = int(input())
cnt = 0
for _ in range(N):
    S = input().strip()
    if S in promise:
        cnt += 1
if cnt == N: print('No') 
else: print('Yes')