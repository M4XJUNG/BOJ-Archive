# 10808 알파벳 개수 2026-02-02(월) 오후 12:22
import sys
input = sys.stdin.readline

S = input().strip() # 개행문자 제거 필수
alphabet = "abcdefghijklmnopqrstuvwxyz"

# 알파벳을 하나씩 돌면서 S 안에 몇 개 있는지 셉니다.
for i in alphabet:
    print(S.count(i), end=' ')