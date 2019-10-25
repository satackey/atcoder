a, b = map(int, input().split())
if a > b:
    print(a + max(a-1, b))
else:
    print(b + max(a, b-1))
