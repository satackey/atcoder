import bisect

n, q = map(int, input().split())
s = input()
spells = [input().split() for _ in range(q)]

finally_positions = []

for golem_pos in range(-1, n+1):
    for t, d in spells:
        if 0 <= golem_pos < n and s[golem_pos] == t:
            golem_pos += 1 if d == "R" else -1
    finally_positions.append(golem_pos)

left = bisect.bisect_right(finally_positions, -1)
right = bisect.bisect_left(finally_positions, n)

print(right - left)

pass
