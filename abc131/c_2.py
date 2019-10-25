def gcd(a_, b_):
    while b_ != 0:
        a_, b_ = b_, a_ % b_
    return a_


def lcm(a_, b_):
    return a_ * b_ // gcd(a_, b_)


a, b, c, d = map(int, input().split())

c_count = b // c - (a-1) // c
d_count = b // d - (a-1) // d
cd_lcm = lcm(c, d)
cd_count = b // cd_lcm - (a-1) // cd_lcm

ans = 1 + b - a - (c_count + d_count - cd_count)
print(ans)
