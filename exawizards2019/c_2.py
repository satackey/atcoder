n, q = map(int, input().split())
s = input()
spells = [input().split() for _ in range(q)]

current_l = -1
current_r = n

for t, d in reversed(spells):

    if 0 <= current_l + 1 < n and t == s[current_l + 1] and d == "L":
        current_l += 1
    elif 0 <= current_l - 1 < n and t == s[current_l - 1] and d == "R":
        current_l -= 1
    #
    # if 0 <= current_r - 1 < n and t == s[current_r - 1] and d == "R":
    #     current_r -= 1
    # elif 0 <= current_r + 1 < n and t == [current_r + 1] and d == "L":
    #     current_r += 1

    if 0 <= current_r + 1 < n and t == [current_r + 1] and d == "L":
        current_r += 1
    elif 0 <= current_r - 1 < n and t == s[current_r - 1] and d == "R":
        current_r -= 1

print(max(current_r - current_l - 1, 0))
