a, b, c, d = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if a <= i <= b:
                divisors.append(i)
            if i != n // i:
                if a <= n // i <= b:
                    divisors.append(n//i)
    # divisors.sort()
    return divisors


c_divs = make_divisors(c)
d_divs = make_divisors(d)

hoge = set(range(a, b+1)) - set(c_divs) - set(d_divs)
print(len(hoge))



