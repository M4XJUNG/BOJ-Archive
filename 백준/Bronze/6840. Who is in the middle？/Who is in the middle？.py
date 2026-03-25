a = int(input())
b = int(input())
c = int(input())
n = [a, b, c]
n.remove(max(n))
n.remove(min(n))
print(n.pop())