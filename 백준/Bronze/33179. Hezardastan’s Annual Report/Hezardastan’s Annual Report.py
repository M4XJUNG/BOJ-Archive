import sys
pages = map(int, sys.stdin.read().split()[1:])
print(sum((p + 1) // 2 for p in pages))