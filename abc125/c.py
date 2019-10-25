def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


n = int(input())
numbers = list(map(int, input().split()))

divisor_num = {}
for number in numbers:
    divisors = make_divisors(number)

    for divisor in divisors:
        if divisor in divisor_num:
            divisor_num[divisor] += 1
        else:
            divisor_num[divisor] = 1

res = 1
for k, v in divisor_num.items():
    if v == n or v == n-1:
        res = max(res, k)

print(res)
