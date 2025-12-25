# 30794 가희와 클럽 오디션 1
import sys
input = sys.stdin.readline
n, decision = input().split()
score_decision = {
    'miss': 0,
    'bad': 200,
    'cool': 400,
    'great': 600,
    'perfect': 1000
}
print(score_decision[decision] * int(n))