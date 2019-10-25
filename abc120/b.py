a, b, k = map(int, input().split())

count = 0
i = 1
dividable_numbers = []
while True:
    if a % i == 0 and b % i == 0:
        count += 1
        dividable_numbers.append(i)

    if a < i or b < i:
        break

    i += 1

print(dividable_numbers[-k])