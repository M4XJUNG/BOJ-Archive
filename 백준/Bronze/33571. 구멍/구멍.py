# 33571 구멍 2026-01-20(화) 오전 12:33
import sys
input = sys.stdin.readline
S = input()
dimigo = {
    'A' : 1, 'a' : 1, 'B' : 2, 'b' : 1, 'C' : 0, 'c' : 0, 'D' : 1, 'd' : 1, 'E' : 0, 'e' : 1, 'F' : 0, 'f' : 0, 'G' : 0, 'g' : 1, 'H' : 0, 'h' : 0, 'I' : 0, 'i' : 0, 'J' : 0, 'j' : 0, 'K' : 0, 'k' : 0, 'L' : 0, 'l' : 0, 
    'M' : 0, 'm' : 0, 'N' : 0, 'n' : 0, 'O' : 1, 'o' : 1, 'P' : 1, 'p' : 1, 'Q' : 1, 'q' : 1, 'R' : 1, 'r' : 0, 'S' : 0, 's' : 0, 'T' : 0, 't' : 0, 'U' : 0, 'u' : 0, 'V' : 0, 'v' : 0, 'W' : 0, 'w' : 0, 'X' : 0, 'x' : 0, 
    'Y' : 0, 'y' : 0, 'Z' : 0, 'z' : 0, '@' : 1
}
cnt = 0
for i in range(len(S)):
  if S[i] == ' ': continue
  cnt += dimigo.get(S[i], 0)
print(cnt)