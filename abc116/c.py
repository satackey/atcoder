flowers_num = int(input())
target_heights = list(map(int, input().split()))

max_height = max(target_heights)

watering_sum = 0
for row_i in range(1, max_height + 1):
    should_water = False

    for target_height in target_heights:
        if row_i <= target_height:
            should_water = True
        elif should_water:
                watering_sum += 1
                should_water = False

    if should_water:
        watering_sum += 1
        should_water = False

print(watering_sum)
