# 14038_Tournament Selection
games = []
for _ in range(6):
    games.append(input())
win = games.count('W')
if win == 5 or win == 6: print(1)
elif win == 3 or win == 4: print(2)
elif win == 1 or win == 2: print(3)
elif win == 0: print(-1)