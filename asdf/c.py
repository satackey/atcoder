n = int(input())
s = input()

replace_dot_result = 0
replace_sharp_result = 0
is_before_white_only = True
for char in s:
    if char == "#":
        is_before_white_only = False
        replace_sharp_result += 1

    elif not is_before_white_only and char == ".":
        replace_dot_result += 1

print(min(replace_dot_result, replace_sharp_result))
