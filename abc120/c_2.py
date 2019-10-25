cubes = input()

removed_cubes_count = 0

while True:
    count01 = cubes.count('01')
    count10 = cubes.count('10')

    if count01 == 0 and count10 == 0:
        break

    removed_cubes_count += count01 + count10
    print(cubes)
    cubes = cubes.translate({
        '01': '',
        '10': ''
    })



print(removed_cubes_count)
