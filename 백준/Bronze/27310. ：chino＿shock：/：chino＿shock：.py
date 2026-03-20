# 27310_:chino_shock:
emoji = input()
cnt = 0
cnt += len(emoji) + emoji.count(':') + (emoji.count('_') * 5)
print(cnt)