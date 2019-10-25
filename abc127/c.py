n, m = map(int, input().split())
lrs = [list(map(int, input().split())) for _ in range(m)]

l_max = 1
r_min = n
for l, r in lrs:
    l_max = max(l, l_max)
    r_min = min(r, r_min)

print(max(r_min - l_max + 1, 0))
