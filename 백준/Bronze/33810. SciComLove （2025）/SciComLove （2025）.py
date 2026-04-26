target = "SciComLove"
s = input().strip()
print(sum(a != b for a, b in zip(target, s)))