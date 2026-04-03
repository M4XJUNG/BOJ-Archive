# 13623_Zero or One
players = list(map(int, input().split()))
if sum(players) == 1: 
    if players.index(1) == 0: print('A')
    elif players.index(1) == 1: print('B')
    else: print('C')
elif sum(players) == 2: 
    if players.index(0) == 0: print('A')
    elif players.index(0) == 1: print('B')
    else: print('C')
else: print('*')