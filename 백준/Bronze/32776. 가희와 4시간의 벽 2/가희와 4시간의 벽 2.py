# 32776 가희와 4시간의 벽 2 2026-01-19(월) 오후 11:15
import sys
input = sys.stdin.readline
s_ab = int(input())
m_a, f_ab, m_b = map(int, input().split())
flight = m_a + f_ab + m_b
if s_ab <= 240 or s_ab <= flight: print('high speed rail')
else: print('flight')