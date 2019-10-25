mod = 1000000007


def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


n = int(input())
s = input()

for i in range(0, n - 1):
    pass

# ans = (2 ** n - 1) % mod
print(modpow(2, n, mod) - 1)
