n, q = map(int, input().split())
s = "_{}_".format(input())
td = [input().split() for _ in range(q)]

current_l = 0
current_r = len(s) - 1

for t, d in reversed(td):

    if current_l + 1 < len(s) - 1 and t == s[current_l + 1] and d == "L":
        current_l += 1
    elif t == s[current_l] and d == "R":
        current_l -= 1

    if 0 < current_r - 1 and t == s[current_r - 1] and d == "R":
        current_r -= 1
    elif t == s[current_r] and d == "L":
        current_r += 1

print(max(current_r - current_l - 1, 0))
