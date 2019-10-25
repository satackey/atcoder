n = int(input())
w_s = list(map(int, input().split()))

ans = 100
for i in range(100):
    g1 = w_s[:i]
    g2 = w_s[i:]
    g1s, g2s = sum(g1), sum(g2)

    t = max(g1s-g2s, g2s-g1s)

    ans = min(ans, t)

print(ans)