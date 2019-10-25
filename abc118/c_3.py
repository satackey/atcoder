n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
zero_monster_indexes = []

while True:
    for monster_i in range(1, len(a)):
        if a[monster_i] == 0:
            zero_monster_indexes.append(monster_i)
        else:
            a[monster_i] %= a[0]

            if a[monster_i] == 0:
                zero_monster_indexes.append(monster_i)

    for zero_monster_index in reversed(zero_monster_indexes):
        a.pop(zero_monster_index)
    zero_monster_indexes.clear()

    a = sorted(a)
    if len(a) == 1:
        break

print(a[0])
