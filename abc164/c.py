s_gifts = [input() for _ in range(int(input()))]

gifts_count = {}
for gift in s_gifts:
    if not gift in gifts_count:
        gifts_count[gift] = 0
    gifts_count[gift] += 1

print(len(gifts_count.keys()))
