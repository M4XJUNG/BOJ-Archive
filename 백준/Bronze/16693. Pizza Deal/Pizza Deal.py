# 16693_Pizza Deal
import math
A_1, P_1 = map(int, input().split())
R_1, P_2 = map(int, input().split())
if A_1 * P_2 > (R_1 ** 2 * math.pi) * P_1: print('Slice of pizza')
else: print('Whole pizza')