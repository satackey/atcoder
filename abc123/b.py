import math

cooking_times = [int(input()) for _ in range(5)]

last_order_index = None
last_order_time = 10
for i, cooking_time in enumerate(cooking_times):
    ones_place = int(str(cooking_time)[-1])
    if last_order_time > ones_place != 0:
        last_order_time = ones_place
        last_order_index = i

time = 0
for i, cooking_time in enumerate(cooking_times):
    if i == last_order_index:
        time += cooking_time
    else:
        time += int(math.ceil(cooking_time / 10) * 10)

print(time)