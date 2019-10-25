n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = []

ok_count = 0

for i in range(n):
    a.append(list(map(int, input().split())))

    sum = c
    for j in range(m):
        sum += a[i][j] * b[j]

    ok_count += 1 if sum > 0 else 0

print(ok_count)
