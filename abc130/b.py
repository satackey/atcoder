n, x = map(int, input().split())
ls = list(map(int, input().split()))

count = 1
current = 0
for l in ls:
    current += l
    if x >= current:
        count += 1
    else:
        break
print(count)
