a, b, c = map(int, input().split())

count = 0

while True:
    if count == c:
        break
    if a * (1 + count) <= b:
        count += 1
    else:
        break

print(count)