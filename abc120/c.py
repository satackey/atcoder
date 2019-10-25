cubes = input()

removed_cubes_count = 0

while True:
    remove_index01 = cubes.find('01')
    if remove_index01 >= 0:
        cubes = cubes[:remove_index01] + cubes[remove_index01 + 2:]
        removed_cubes_count += 2


    remove_index10 = cubes.find('10')
    if remove_index10 >= 0:
        cubes = cubes[:remove_index10] + cubes[remove_index10 + 2:]
        removed_cubes_count += 2

    if remove_index01 == -1 and remove_index10 == -1:
        break

print(removed_cubes_count)
