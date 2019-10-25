cubes = input()

deleted_cube_len = 0

char_possible_deleted = cubes[0]
char_possible_deleted_len = 1

deleted_char_len = 0

is_deleting = False

for i in range(1, len(cubes)):
    if not is_deleting:
        # 数えている文字が続いているとき
        if char_possible_deleted == cubes[i]:
            # 数える
            char_possible_deleted_len += 1
        else:
            is_deleting = True

    if is_deleting:
        if char_possible_deleted_len > deleted_char_len and char_possible_deleted != cubes[i]:
            deleted_char_len += 1
            deleted_cube_len += 2

        else:
            char_possible_deleted = cubes[i]
            char_possible_deleted_len = 1
            deleted_char_len = 0
            is_deleting = False

print(deleted_cube_len)



