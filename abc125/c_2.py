import math
from functools import reduce
import copy


def gcd(*nums):
    return reduce(math.gcd, nums)


n = int(input())
numbers = list(map(int, input().split()))

res = 1
for i in range(n):
    numbers_copy = copy.copy(numbers)
    numbers_copy.pop(i)

    res = max(res, gcd(numbers_copy))

