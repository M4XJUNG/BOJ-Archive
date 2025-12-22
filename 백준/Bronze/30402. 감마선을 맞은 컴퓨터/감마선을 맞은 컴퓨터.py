# 30402 감마선을 맞은 컴퓨터
import sys
input = sys.stdin.readline
print_image = ''
for _ in range(15):
  image = list(input().split())
  if 'w' in image: print_image = 'chunbae'
  elif 'b' in image: print_image = 'nabi'
  elif 'g' in image: print_image = 'yeongcheol'
print(print_image)