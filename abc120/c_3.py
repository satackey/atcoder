import time
cubes = input()

removed_cubes_count = 0

start = time.time()
while True:
    # removed_cubes = cubes
    removed_cubes = cubes.replace('10', '').replace('01', '')
    removed_cubes_count += len(cubes) - len(removed_cubes)
    if len(cubes) == len(removed_cubes):
        break

    cubes = removed_cubes

print("all elapsed_time:{0}".format(time.time() - start) + "[sec]")
print(removed_cubes_count)
