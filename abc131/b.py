n, l = map(int, input().split())

apples = range(l, n+l)
print(sum(sorted(apples, key=lambda x: abs(x))[1:]))
