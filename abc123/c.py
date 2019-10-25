import math

n = int(input())
limits = [int(input()) for _ in range(5)]

limit = min(limits)

min_time = 5
min_time += math.ceil((n - limit) / limit)

print(min_time)
