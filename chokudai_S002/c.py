n = int(input())
sums = []
for i in range(n):
    a, b = map(int, input().split())
    sums.append(a + b)
print(max(sums))
