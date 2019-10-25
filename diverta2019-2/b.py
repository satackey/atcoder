n = int(input())
xys = [list(map(int, input().split())) for _ in range(n)]

pqs = {}

for i in range(n):
    for j in range(i + 1, n):
        p = xys[j][0] - xys[i][0]
        q = xys[j][1] - xys[i][1]

        if p == 0 or q == 0:
            continue

        p = max(p, -p)
        q = max(q, -q)

        string = str(p) + " " + str(q)
        if string not in pqs:
            pqs[string] = 0

        pqs[string] += 1


# p, q = map(int, max(pqs.items(), key=lambda x: x[1])[0].split())

print(max(n - max(pqs.values()), 1) if len(pqs) != 0 else n)
