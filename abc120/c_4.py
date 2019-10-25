cubes = input()

removed_cubes_count = 0
counted_char = cubes[0]
counted_char_len = 1
deleted_char_len = 0
is_deleting = False

for i in range(1, len(cubes)):
    if not is_deleting:
        if counted_char == cubes[i]:
            counted_char_len += 1
        else:
            is_deleting = True

    if is_deleting:
        if counted_char != cubes[i]:
            counted_char = cubes[i]
            counted_char_len = 0
            deleted_char_len = 0
            is_deleting = False

        if counted_char_len > deleted_char_len:

            deleted_char_len += 1
            removed_cubes_count += 2
        else:
            counted_char = cubes[i]
            counted_char_len = 0
            deleted_char_len = 0
            is_deleting = False

print(removed_cubes_count)
