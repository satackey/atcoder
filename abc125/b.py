n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

print(sum([v[i] - c[i] for i in range(n) if v[i] - c[i] > 0]))

# for i, pair in enumerate(pairs):
