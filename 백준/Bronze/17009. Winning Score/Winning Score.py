A_3 = int(input())
A_2 = int(input())
A_1 = int(input())
B_3 = int(input())
B_2 = int(input())
B_1 = int(input())

A_total = A_3 * 3 + A_2 * 2 + A_1
B_total = B_3 * 3 + B_2 * 2 + B_1

if A_total > B_total:
    print('A')
elif A_total < B_total:
    print('B')
else:
    print('T')