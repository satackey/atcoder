n, m = map(int, input().split())
a_s = [int(input()) for _ in range(m)]

dp = [1]
n_with_a = [[i, False] for i in range(n+1)]

for a in a_s:
    n_with_a[a][1] = True

dp.append(0 if n_with_a[1][1] else 1)

for i, is_broken in n_with_a[2:]:
    if is_broken:
        dp.append(0)
    else:
        dp.append((dp[i-1] + dp[i-2]) % 1000000007)

print(dp[-1])
