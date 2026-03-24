# 5357_Dedupe
N = int(input())
for _ in range(N):
    s = input()
    ans = s[0] 
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ans += s[i]
    print(ans)