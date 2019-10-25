n = int(input())
a = list(map(int, input().split()))

can_continue = True
count = 0

while can_continue:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] /= 2
        else:
            can_continue = False
            continue
    if can_continue:
        count += 1

print(count)
